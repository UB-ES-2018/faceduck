import uuid
from faceduck.models.friendship import Friendship
from faceduck.models.user import User
from faceduck.utils import FaceduckError
from elasticsearch.exceptions import NotFoundError


def exists_friendship(user_id, target_id):
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
    }).doc_type(Friendship).execute()

    if len(friendship) == 0:
        if len(friendship2) == 0:
            return False
        return friendship2.hits[0]
    else:
        return friendship.hits[0]


def create_friendship(user_id, target_id, state='pending'):
    if User.get(id=user_id, ignore=404) is None or User.get(id=target_id, ignore=404) is None:
        raise FaceduckError("001")

    if exists_friendship(user_id, target_id):
        raise FaceduckError("001")

    friendship = Friendship(meta={'id': uuid.uuid4()}, user_id=user_id, target_id=target_id, state=state)
    friendship.save()

    return friendship


def delete_friendship(user_id, target_id):
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

    if len(friendship) != 0:
        for entry in friendship:
            entry.delete()
    
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
    }).doc_type(Friendship).execute()

    if len(friendship2) != 0:
        for entry in friendship2:
            entry.delete()


def update_friendship(user_id, target_id, state):
    states = ['friends']
    if state not in states:
        raise FaceduckError("001")

    if User.get(id=user_id, ignore=404) is None or User.get(id=target_id, ignore=404) is None:
        raise FaceduckError("001")

    friendship = exists_friendship(target_id, user_id)
    
    if friendship is False:
        raise FaceduckError("001")

    friendship.state = state
    friendship.save()
    return friendship


def get_friends(user_id):
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
    
    return friends


def get_full_friends(user_id):
    try:
        friends = Friendship.search().from_dict({
            "query": {
                "bool": {
                    "must": {
                        "match": {
                            "state": "friends"
                        }
                    },
                    "should": [
                        {
                            "multi_match": {
                                "query": user_id,
                                "fields": ["user_id", "target_id"]
                            }
                        }
                    ]
                }
            }
        }).doc_type(Friendship).execute()
    except NotFoundError:
        raise FaceduckError("001")

    return friends


def get_full_friend_ids(user_id):
    friends = get_full_friends(user_id)
    return [f.target_id for f in friends if f.state == 'friends']
