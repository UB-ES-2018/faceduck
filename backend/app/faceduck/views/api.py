from flask import make_response, request, jsonify
from faceduck.blueprints import api
from faceduck import core
from faceduck.utils import FaceduckError
from flask_jwt_extended import jwt_required, jwt_optional, current_user
from .mappers import user_mapper, post_mapper, comment_mapper, friendship_mapper, group_mapper, log_mapper
from faceduck.views.view_utils import client_error


@api.route('/user', methods=["POST"])
def signup():
    if not request.is_json:
        return client_error("001")
    
    try:
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        name = request.json['name']
        surname = request.json['surname']
        birthday = request.json['birthday']
        gender = request.json['gender']
    except KeyError:
        return client_error("001")

    try:
        user = core.create_user(username, email, password, name,
                                surname, birthday, gender)
    except FaceduckError as e:
        return client_error(e.id)
    
    return ("", 204)


@api.route('/session', methods=["POST"])
def login():
    req = request.get_json()
    device = request.headers.get('User-Agent')
    ip = request.remote_addr
    try:
        email = req['email']
        password = req['password']
    except KeyError:
        return client_error("001")
    try:
        user, token = core.login_user(email, password, device, ip)
        return jsonify({
            'user': user_mapper(user),
            'access-token': token
        })
    except FaceduckError as e:
        return client_error(e.id)


@api.route("/post", methods=["POST"])
@jwt_required
def create_post():
    if not request.is_json:
        return client_error("001")

    author_id = current_user.meta.id

    try:
        text = request.json["text"]
        image_url = request.json.get("image-url", None)
        visibility = request.json.get("visibility", "public")
    except KeyError:
        return client_error("001")

    try:
        post = core.create_post(text, author_id, image_url, visibility)
        response = post_mapper(post)
    except FaceduckError as e:
        return client_error(e.id)
    
    return jsonify(response)


@api.route("/post/<post_id>")
@jwt_optional
def get_post(post_id):
    try:
        user_id = (current_user or None) and current_user.meta.id
        post = core.get_post(post_id, user_id)
        response = post_mapper(post)
    except FaceduckError as e:
        return client_error(e.id)

    return jsonify(response)


@api.route('/user/search', methods=["POST"])
@jwt_required
def search_users():
    content = request.get_json()
    
    try:
        query = content['query']
    except KeyError:
        return client_error("001")

    users = core.search_users(query)
    return jsonify([user_mapper(u) for u in users])

@api.route('/group/search', methods=["POST"])
@jwt_required
def search_groups():
    content = request.get_json()
    
    try:
        query = content['query']
    except KeyError:
        return client_error("001")

    groups = core.search_groups(query)
    return jsonify([group_mapper(g) for g in groups])


@api.route('/post/search', methods=["POST"])
@jwt_required
def search_posts():
    content = request.get_json()
    user_id = current_user.meta.id
    
    if "query" in content.keys():
        query = content["query"]
        posts = core.search_posts(query, user_id)
    elif "author-id" in content.keys():
        author_id = content["author-id"]
        posts = core.search_posts_by_author(author_id, user_id)
    elif "tag" in content.keys():
        tag = content["tag"]
        posts = core.search_posts_by_tag(tag, user_id)
    else:
        return client_error("001")
    try:
        return jsonify([post_mapper(p) for p in posts])
    except FaceduckError as e:
        return client_error(e.id)


@api.route('/user/friends/<user_id>/<target_id>')
@jwt_required
def get_friendship(user_id, target_id):
    friendship = core.exists_friendship(user_id,target_id)

    try:
        if not friendship:
            return jsonify(
                user_id=user_id,
                target_id=target_id,
                state="not-friends"
            )
        else:
            return jsonify(friendship_mapper(friendship))
    except FaceduckError as e:
        return client_error(e.id)


@api.route('/user/friends', methods=["POST"])
@jwt_required
def create_friendship():
    try:
        user_id = current_user.meta.id

        target_id = request.json["target_id"]
    except KeyError:
        return client_error("001")
    
    try:
        friendship = core.create_friendship(user_id, target_id)
        return jsonify(friendship_mapper(friendship))
    except FaceduckError as e:
        return client_error(e.id)


@api.route('/user/friends', methods=["PUT"])
@jwt_required
def update_friendship():
    try:
        user_id = current_user.meta.id
        target_id = request.json["target_id"]
        state = request.json["state"]
    except KeyError:
        return client_error("001")

    try:
        friendship = core.update_friendship(user_id, target_id, state=state)
        return jsonify(friendship_mapper(friendship))
    except FaceduckError as e:
        return client_error(e.id)


@api.route('/user/friends', methods=["DELETE"])
@jwt_required
def delete_friendship():
    try:
        user_id = current_user.meta.id
        target_id = request.json["target_id"]
    except KeyError:
        return client_error("001")
    
    core.delete_friendship(user_id,target_id)
    return ("", 204)


@api.route('/user/friends/<user_id>')
@jwt_required
def get_friends(user_id):
    full_users = request.args.get('full', False, type=bool)

    if full_users:
        friends = core.get_full_friend_ids(user_id)
        users = [core.get_user(f) for f in friends]  # OPTIMIZE
        return jsonify([user_mapper(u) for u in users])
    else:
        friends = core.get_friends(user_id)
        return jsonify([friendship_mapper(f) for f in friends])


@api.route('/user/friends/', methods=["GET"])
@jwt_required
def get_friends_full():
    user_id = current_user.meta.id
    friends = core.get_full_friend_ids(user_id)
    users = [core.get_user(f) for f in friends]#OPTIMIZE
    return jsonify([user_mapper(u) for u in users])


@api.route("/post/<post_id>/reactions", methods=["POST"])
@jwt_required
def add_reactions(post_id):
    try:
        user_id = current_user.meta.id
        reaction = request.json["reaction"]
        core.set_reaction(post_id, user_id, reaction)
        response = get_post(post_id)

    except KeyError:
        return client_error("001")
    except FaceduckError as e:
        return client_error(e.id)
    return response


@api.route("/post/<post_id>/reactions", methods=["DELETE"])
@jwt_required
def delete_reactions(post_id):
    try:
        user_id = current_user.meta.id
        core.delete_reaction(post_id,user_id)
    except FaceduckError as e:
        return client_error(e.id)
    return ("",204)


@api.route("/post/<post_id>/comments", methods=["GET"])
@jwt_optional
def get_comments(post_id):
    try:
        user_id = (current_user or None) and current_user.meta.id
        core.get_post(post_id, user_id)
        cmts = core.get_comments(post_id, None)

        return jsonify([comment_mapper(c) for c in cmts])
    except FaceduckError as e:
        return client_error(e.id)


@api.route("/post/<post_id>/comments", methods=["POST"])
@jwt_required
def add_comment(post_id):
    try:
        user_id = current_user.meta.id
        text = request.json["text"]
        if text!="":
            response = core.add_comment(post_id, user_id, text)
        else:
            return client_error("001")
    except KeyError:
        return client_error("001")
    except FaceduckError as e:
        return client_error(e.id)
    return jsonify(comment_mapper(response))


@api.route("/post/<post_id>/comments", methods=["DELETE"])
@jwt_required
def remove_comment(post_id):
    try:
        user_id = current_user.meta.id
        comment_id = request.json["comment_id"]
        core.remove_comment(post_id, comment_id, user_id)
    except KeyError:
        return client_error("001")
    except FaceduckError as e:
        return client_error(e.id)
    return ("",204)


@api.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = core.get_user(user_id)
    return jsonify(user_mapper(user))


@api.route("/post/newsfeed")
@jwt_required
def get_newsfeed():
    user_id = current_user.meta.id

    newsfeed = core.get_newsfeed(user_id)

    return jsonify([post_mapper(p) for p in newsfeed])


@api.route("/login_logs")
@jwt_required
def get_login_logs():
    user_id = current_user.meta.id
    
    try:
        logs = core.get_login_logs(user_id)
    except FaceduckError as e:
        return client_error(e.id)
    
    return jsonify([log_mapper(p) for p in logs])


@api.route("/group", methods=["POST"])
@jwt_required
def create_group():
    user_id = current_user.meta.id
    try:
        name = request.json["name"]
    except KeyError:
        return client_error("001")
    if "image-url" in request.get_json().keys():
        image_url = request.json["image-url"]
    else:
        image_url = ""
    group = core.create_group(name,image_url,user_id)
    return jsonify(group_mapper(group))


@api.route("/group/<group_id>", methods=["GET"])
def get_group(group_id):
    return jsonify(group_mapper(core.get_group(group_id)))


@api.route("/group/<group_id>", methods=["DELETE"])
@jwt_required
def remove_group(group_id):
    core.remove_group(group_id)
    return ("",204)


@api.route("/group/<group_id>/posts", methods=["GET"])
def get_posts(group_id):
    posts = core.get_group_posts(group_id)

    return jsonify([post_mapper(p) for p in posts])


@api.route("/group/<group_id>/posts", methods=["POST"])
@jwt_required
def create_group_post(group_id):
    user_id = current_user.meta.id
    try:
        text = request.json["text"]
    except KeyError:
        return client_error("001")
    if "image-url" in request.get_json().keys():
        image_url = request.json["image-url"]
    else:
        image_url = ""
    post = core.create_group_post(group_id,user_id,text,image_url)
    return jsonify(post_mapper(post))


@api.route("/group/<group_id>/posts/<post_id>", methods=["GET"])
def get_group_post(group_id,post_id):
    return jsonify(post_mapper(core.get_group_post(post_id)))


@api.route("/group/<group_id>/posts/<post_id>", methods=["DELETE"])
@jwt_required
def remove_group_post(group_id,post_id):
    core.remove_group_post(group_id,post_id)
    return ("",204)


@api.route("/group/<group_id>/members", methods=["GET"])
@jwt_required
def get_group_members(group_id):
    members = core.get_group_members(group_id)
    return jsonify([user_mapper(core.get_user(m)) for m in members])


@api.route("/group/<group_id>/members/admins", methods=["GET"])
@jwt_required
def get_group_admins(group_id):
    admins = core.get_group_admins(group_id)
    return jsonify([user_mapper(core.get_user(a)) for a in admins])


@api.route("/group/<group_id>/members", methods=["POST"])
@jwt_required
def add_user_to_group(group_id):
    if "user_id" in request.get_json().keys():
        user_id = request.json["user_id"]
    else:
        user_id = current_user.meta.id

    core.add_user_to_group(group_id,user_id)
    return ("",204)


@api.route("/group/<group_id>/members", methods=["PUT"])
@jwt_required
def change_user_role(group_id):
    if "user_id" in request.get_json().keys():
        user_id = request.json["user_id"]
    else:
        user_id = current_user.meta.id

    try:
        admin = request.json["admin"]
    except KeyError:
        return client_error("001")
    core.change_user_role(group_id,user_id,admin)
    return("",204)


@api.route("/group/<group_id>/members/<user_id>", methods=["DELETE"])
@jwt_required
def remove_group_member(group_id,user_id):
    core.remove_group_member(group_id,user_id)
    return ("", 204)


@api.route('/user', methods=["PUT"])
@jwt_required
def edit_user():
    if not request.is_json:
        return client_error("001")
    try:
        user = core.edit_user(current_user.meta.id, request.json)
    except FaceduckError as e:
        return client_error(e.id)
    
    return (jsonify(user_mapper(user)))


@api.route('/user/<user_id>/groups', methods=["GET"])
@jwt_required
def get_groups(user_id):
    try:
        gs = core.get_groups(user_id)
        groups = [core.get_group(g) for g in gs]
    except FaceduckError as e:
        return client_error(e.id)
    
    return (jsonify([group_mapper(g) for g in groups]))