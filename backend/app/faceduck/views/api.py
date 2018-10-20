from flask import make_response, request, jsonify
from faceduck.blueprints import api
from faceduck import core
from faceduck.utils import FaceduckError
from flask_jwt_extended import jwt_required
from .mappers import user_mapper, post_mapper
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
    try:
        email = req['email']
        password = req['password']
    except KeyError:
        return client_error("001")
    try:
        user, token = core.login_user(email, password)
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
    
    try:
        text = request.json["text"]
        author_id = request.json["author-id"]
        image_url = request.json.get("image-url", None)
    except KeyError:
        return client_error("001")

    try:
        post = core.create_post(text, author_id, image_url)
        response = post_mapper(post)
    except FaceduckError as e:
        return client_error(e.id)
    
    return jsonify(response)


@api.route("/post/<post_id>")
@jwt_required
def get_post(post_id):
    try:
        post = core.get_post(post_id)
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


@api.route('/post/search', methods=["POST"])
@jwt_required
def search_posts():
    content = request.get_json()

    try:
        query = content['query']
    except KeyError:
        return client_error("001")

    posts = core.search_posts(query)
    
    try:
        return jsonify([post_mapper(p) for p in posts])
    except FaceduckError as e:
        return client_error(e.id)


@api.route('/user/friends', methods=["POST"])
@jwt_required
def create_friendship():

    try:
        user_id = request.json["user_id"]
        target_id = request.json["target_id"]
    except KeyError:
        return client_error("001")

    friendship = core.create_friendship(user_id,target_id)

    try:
        return jsonify(user_id=friendship.user_id, target_id=friendship.target_id,state=friendship.state)
    except FaceduckError as e:
        return client_error(e.id)

@api.route('/user/friends', methods=["PUT"])
@jwt_required
def update_friendship():

    try:
        user_id = request.json["user_id"]
        target_id = request.json["target_id"]
        state = request.json["state"]
    except KeyError:
        return client_error("001")

    friendship = core.update_friendship(user_id,target_id,state)

    try:
        return jsonify(user_id=friendship.user_id, target_id=friendship.target_id,state=friendship.state)
    except FaceduckError as e:
        return client_error(e.id)

@api.route('/user/friends', methods=["DELETE"])
@jwt_required
def delete_friendship():

    try:
        user_id = request.json["user_id"]
        target_id = request.json["target_id"]
    except KeyError:
        return client_error("001")

    friendship = core.delete_friendship(user_id,target_id)

    try:
        return jsonify(status="Friendship deleted")
    except FaceduckError as e:
        return client_error(e.id)



@api.route('/user/friends/<user_id>')
@jwt_required
def get_friends(user_id):
    try:
        friends = core.get_friends(user_id)
    except FaceduckError as e:
        return client_error(e.id)

    try:
        return jsonify([user_mapper(f) for f in friends])
    except FaceduckError as e:
        return client_error(e.id)
