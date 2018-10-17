from faceduck.core.user import get_user

ERRORS = {
    "001": {"error-id": "001", "error-message": "Invalid data"},
    "002": {"error-id": "002", "error-message": "Already existing username"},
    "003": {"error-id": "003", "error-message": "Already existing email"},
    "004": {"error-id": "004", "error-message": "This email or password is invalid"}
}


def user_mapper(user):
    user_dict = {"id": user.meta.id}

    for attr in dir(user):
        key = attr.replace("_", "-")
        
        if attr != "password":
            user_dict[key] = getattr(user, attr)

    return user_dict


def post_mapper(post):
    post_dict = {"id": post.meta.id}
    
    for attr in dir(post):
        key = attr.replace("_", "-")
        
        if attr == "author":
            user = get_user(getattr(post, attr))
            user_dict = user_mapper(user)
            post_dict[key] = user_dict
        else:
            post_dict[key] = getattr(post, attr)

    return post_dict

