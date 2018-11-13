from datetime import datetime
import uuid
import re
from elasticsearch.exceptions import NotFoundError
from faceduck.models.post import Post
from faceduck.models.post import Reaction
from faceduck.models.user import User
from faceduck.utils import FaceduckError
from elasticsearch_dsl import Search
from .social_card import social_card_image


def create_post(text, author_id, image_url, visibility):
    id = uuid.uuid4()
    created_at = str(datetime.now().time())
    split_post = text.split(' ')
    tags = []
    for word in split_post:
        word = remove_punct(word)
        if word[0] == '#':
            tags.append(word)
    if User.get(id=author_id, ignore=404) is None:
        raise FaceduckError("001")

    if image_url is None:
        image_url = social_card_for_post(text)

    post = Post(
        meta={'id': id},
        text=text,
        created_at=created_at,
        author=author_id,
        image_url=image_url,
        tags=tags,
        visibility=visibility
    )

    post.save(refresh=True)

    return post


def social_card_for_post(text):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+', text)
    if len(urls) == 0:
        return
    # We're going to parse just the first
    url = urls[0]
    return social_card_image(url)


def get_post(post_id):
    try:
        post = Post.get(id=post_id)
    except NotFoundError:
        raise FaceduckError("001")
    
    return post

def remove_punct(word):
    new_word = ""
    punct = ['.', ',', '!', '¡', '?', '¿']
    for i in word:
        if i not in punct:
            new_word += i
    return new_word

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

