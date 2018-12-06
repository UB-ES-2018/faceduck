from faceduck.models.post import Post
from .friendship import get_full_friend_ids

START = 0
SIZE = 50


def search_posts(query, user_id, start=START, size=SIZE):
    base_q = {
        "match": {
            "text": query,
        }
    }

    q = generate_search_query(user_id, base_q)

    response = Post.search(q).from_dict(q).doc_type(Post).sort({"created_at": {"order": "desc"}})[start:size].execute()

    return [d for d in response.hits]

def get_all_public_posts():
    response = Post.search().from_dict({
        "query": {
            "match_phrase": {
                "visibility": "public"
            }
        }
    }).doc_type(Post).execute()

    return [p for p in response.hits]

def search_posts_by_author(author, user_id, start=START, size=SIZE):
    base_q = {"match_phrase": {"author": author}}
    q = generate_search_query(user_id, base_q)

    response = Post.search().from_dict(q).doc_type(Post).sort({"created_at": {"order": "desc"}})[start:size].execute()
    
    return [d for d in response.hits]


def search_posts_by_tag(tag, user_id):
    base_q = {
        "match_phrase": {
            "tags": tag
        }
    }
    q = generate_search_query(user_id, base_q)
    response = Post.search().from_dict(q).doc_type(Post).execute()

    return [d for d in response.hits]


def generate_search_query(user_id, q):
    friend_ids = get_full_friend_ids(user_id) + [user_id]

    friend_matches = []

    for f_id in friend_ids:
        friend_matches.append({
            "bool": {
                "must": [
                    {
                        "match_phrase": {
                            "author": f_id
                        }
                    },
                    {
                        "match_phrase": {
                            "visibility": "friends"
                        }
                    }
                ]
            }
        })

    return {
        "query": {
            "bool": {
                "must": q,
                "should": [
                              {
                                  "match_phrase": {
                                      "visibility": "public"
                                  }
                              },
                              {
                                  "bool": {
                                      "must": [
                                          {
                                              "match_phrase": {
                                                  "visibility": "private"
                                              }
                                          },
                                          {
                                              "match_phrase": {
                                                  "author": user_id
                                              }
                                          }
                                      ]
                                  }
                              }
                          ] + friend_matches,
                "minimum_should_match": 1
            }
        }
    }
