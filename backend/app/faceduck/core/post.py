from datetime import datetime
import uuid
from elasticsearch.exceptions import NotFoundError
from faceduck.models.post import Post
from faceduck.models.post import Reaction
from faceduck.models.user import User
from faceduck.utils import FaceduckError
from elasticsearch_dsl import Search

def create_post(text, author_id, image_url):
    id = uuid.uuid4()
    created_at = str(datetime.now().time())
    if User.get(id=author_id, ignore=404) is None:
        raise FaceduckError("001")
    
    post = Post(meta={'id': id}, text=text, created_at=created_at, author=author_id, image_url=image_url)
    post.save()
    
    return post


def get_post(post_id):
    try:
        post = Post.get(id=post_id)
    except NotFoundError:
        raise FaceduckError("001")
    
    return post


def search_reaction(post,user_id):
    query = Search().query('match', user_reaction__user_id=user_id).to_dict()
    response = post.search().from_dict(query).doc_type(Reaction).execute()

    return [d for d in response.hits]

def set_reaction(post_id, user_id, reaction):
    post = get_post(post_id)
    r = search_reaction(post,user_id)
    if len(r):
        post.update_reaction(user_id,reaction)
    else:
        post.add_reaction(user_id, reaction)
    post.save()

def delete_reaction(post_id,user_id):
    post = get_post(post_id)
    post.remove_reaction(user_id)
    post.save()

def add_comment(post_id,user_id,text):
    post = get_post(post_id)
    c = post.add_comment(user_id,text)
    post.save()
    return c

def get_comments(post_id):
    post = get_post(post_id)
    return post.get_comments()

def remove_comment(post_id, comment_id):
    post = get_post(post_id)
    post.remove_comment(comment_id)
    post.save()