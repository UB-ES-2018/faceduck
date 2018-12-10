from .user import get_user
from .post import create_post, get_post, get_post_by_id
import uuid
from faceduck.models.group import Group
from elasticsearch.exceptions import NotFoundError
from faceduck.utils import FaceduckError

def create_group(name,image_url,user_id):
    id = uuid.uuid4()
    group = Group(
        meta={'id': id},
        name=name,
        image_url=image_url,
    )
    user = get_user(user_id)
    group.addUser(user)
    group.makeAdmin(user_id)
    group.save()

    return group

def get_group(group_id):
    try:
        group = Group.get(id=group_id)
    except NotFoundError:
        raise FaceduckError("001")

    return group

def remove_group(group_id):
    group = get_group(group_id)
    for i in group.getUsers():
        group.removeUser(get_user(i))
    group.delete()

def get_group_posts(group_id):
    group = get_group(group_id)
    return [get_post_by_id(p) for p in group.getPosts()]

def create_group_post(group_id, user_id, text, image_url):
    post = create_post(text, user_id, image_url, "public")
    group = get_group(group_id)
    group.addPost(post.meta.id)
    group.save()
    return post;

def get_group_post(post_id):
    return get_post_by_id(post_id)

def remove_group_post(group_id, post_id):
    group = get_group(group_id)
    group.removePost(post_id)
    group.save()
    get_post_by_id(post_id).delete()

def get_group_members(group_id):
    group = get_group(group_id)
    return group.getUsers()

def get_group_admins(group_id):
    group = get_group(group_id)
    return group.getAdmins()

def add_user_to_group(group_id,user_id):
    user = get_user(user_id)
    group = get_group(group_id)
    group.addUser(user)
    group.save()

def make_member_admin(group_id,user_id):
    group = get_group(group_id)
    group.makeAdmin(user_id)
    group.save()

def make_admin_member(group_id,user_id):
    group = get_group(group_id)
    group.makeUser(user_id)
    if len(group.getAdmins()) == 0:
        group.makeAdmin(random.choice(group.getUsers()))
    group.save()

def change_user_role(group_id,user_id,admin):
    if admin:
        make_member_admin(group_id,user_id)
    else:
        make_admin_member(group_id,user_id)

def is_member(group_id,user_id):
    group = get_group(group_id)
    return group.isUser(user_id)

def is_admin(group_id,user_id):
    group = get_group(group_id)
    return group.isAdmin(user_id)

def remove_group_member(group_id,user_id):
    group = get_group(group_id)
    group.removeUser(get_user(user_id))
    if len(group.getUsers()) == 0:
        group.delete()
    else:
        group.save()