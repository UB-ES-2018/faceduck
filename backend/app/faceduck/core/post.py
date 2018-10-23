from datetime import datetime
import uuid
import string
from elasticsearch.exceptions import NotFoundError
from faceduck.models.post import Post
from faceduck.models.user import User
from faceduck.utils import FaceduckError


def create_post(text, author_id, image_url):
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
    
    post = Post(meta={'id': id}, text=text, created_at=created_at, author=author_id, image_url=image_url, tags=tags)
    post.save()
    
    return post


def get_post(post_id):
    try:
        post = Post.get(id=post_id)
    except NotFoundError:
        raise FaceduckError("001")
    
    return post

def remove_punct(word):
    new_word = ""
    punct = ['.',',','!','¡', '?', '¿']
    for i in word:
        if i not in punct:
            new_word += i
    return new_word

