from datetime import datetime
import uuid
from elasticsearch.exceptions import NotFoundError
from faceduck.models.friendship import Friendship
from faceduck.models.user import User
from faceduck.utils import FaceduckError

def exists_friendship(user_id,target_id):
    friendship = Friendship.search().from_dict({
            "query": {
            "bool": {
              "must": [
                {
                  "match": {
                    "user_id": user_id
                  }
                },
                {
                  "match": {
                    "target_id": target_id
                  }
                }
              ]
            }
            }
    }).doc_type(Friendship).execute()

    if len(friendship) == 0:
        return False
    return True


def create_friendship(user_id, target_id, state='pending'):
    id = uuid.uuid4()
    if User.get(id=user_id, ignore=404) is None or User.get(id=target_id, ignore=404) is None:
        raise FaceduckError("001")

    if exists_friendship(user_id,target_id):
        raise FaceduckError("001")

    friendship = Friendship(meta={'id': user_id},user_id=user_id, target_id=target_id, state=state)
    friendship.save()
    
    return friendship


def delete_friendship(user_id,target_id):
    if not exists_friendship(user_id, target_id):
        raise FaceduckError("001")

    friendship = Friendship.search().from_dict({
            "query": {
            "bool": {
              "must": [
                {
                  "match": {
                    "user_id": user_id
                  }
                },
                {
                  "match": {
                    "target_id": target_id
                  }
                }
              ]
            }
            }
    }).doc_type(Friendship).execute().hits[0]

    
    if friendship.state == 'friends':
        friendship2 = Friendship.search().from_dict({
            "query": {
            "bool": {
              "must": [
                {
                  "match": {
                    "user_id": target_id
                  }
                },
                {
                  "match": {
                    "target_id": user_id
                  }
                }
              ]
            }
            }
        }).doc_type(Friendship).execute().hits[0]

        friendship2.delete()

    friendship.delete()

def update_friendship(user_id,target_id,state):
    states = ['pending','friends', 'not-friends']
    if state not in states:
        raise FaceduckError("001")

    if User.get(id=user_id, ignore=404) is None or User.get(id=target_id, ignore=404) is None:
        raise FaceduckError("001")

    friendship = Friendship.search().from_dict({
            "query": {
            "bool": {
              "must": [
                {
                  "match": {
                    "user_id": user_id
                  }
                },
                {
                  "match": {
                    "target_id": target_id
                  }
                }
              ]
            }
            }
    }).doc_type(Friendship).execute().hits[0]

    friendship.state = state
    friendship.save()

    if state == 'friends':
        create_friendship(target_id,user_id,'friends')
        
    return friendship

def get_friends(user_id):
    try:
        friends = Friendship.search().from_dict({
            "query": {
            "bool": {
              "must": [
                {
                  "match": {
                    "user_id": user_id
                  }
                },
                {
                  "match": {
                    "state": "friends"
                  }
                }
              ]
            }
            }
        }).doc_type(Friendship).execute()
    except NotFoundError:
        raise FaceduckError("001")
    
    return friends

