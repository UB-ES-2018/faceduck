from datetime import datetime
import uuid
from elasticsearch.exceptions import NotFoundError
from faceduck.models.post import Post
from faceduck.models.post import Reaction
from faceduck.models.user import User
from faceduck.utils import FaceduckError


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
    response = post.search().from_dict({
        "query": {
            "nested": {
                "path": "user_reaction", 
                "query": {
                    "match" : {
                        "user_reaction.user_id" : user_id
                    }
                }
            }
            
        }
    }).doc_type(Reaction).execute()


    return [d for d in response.hits]

def set_reaction(post_id, user_id, reaction):
    post = get_post(post_id)
    #if len(search_reaction(post,user_id)):
    #    post.user_reaction.reaction = reaction
    #else:
    
    post.add_reaction(user_id, reaction)
    post.save()

