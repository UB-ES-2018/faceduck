from faceduck.models.user import User
from faceduck.core.sessionkeeping import SessionKeeping
from werkzeug.security import check_password_hash
from faceduck.utils import FaceduckError


def get_user_by_email(email):
    email_response = User.search().from_dict({
         "query": {
             "match_phrase": {
                 "email": email
             }
         }
     }).doc_type(User).execute()

    if len(email_response.hits) == 0:
        return None

    return email_response.hits[0]


def login_user(email, password):
    user = get_user_by_email(email)

    if user is None:
        raise FaceduckError("004")

    if not check_password_hash(user.password, password):
        raise FaceduckError("004")

    token = SessionKeeping.generate_jwt_token(user.meta.id)

    return user, token
