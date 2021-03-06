from faceduck.models.user import User
from faceduck.core.sessionkeeping import SessionKeeping
from werkzeug.security import check_password_hash
from faceduck.utils import FaceduckError
import datetime


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


def login_user(email, password, device, ip):
    user = get_user_by_email(email)

    if user is None:
        raise FaceduckError("004")

    if not check_password_hash(user.password, password):
        add_log(user, device, ip, False)
        raise FaceduckError("004")

    token = SessionKeeping.generate_jwt_token(user.meta.id)

    add_log(user, device, ip, True)

    return user, token

def add_log(user, device,ip, state):
    time = datetime.datetime.now()
    #time2 = time.srftime("%Y-%m-%d %H:%M")
    user.add_log(device, ip, state, time)
    user.save()
