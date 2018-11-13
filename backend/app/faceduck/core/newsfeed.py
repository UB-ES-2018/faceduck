from .friendship import get_full_friend_ids
from faceduck.models.post import Post


def get_newsfeed(user_id):
    friend_ids = get_full_friend_ids(user_id)

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

    q = {
        "query": {
            "bool": {
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

    response = Post.search().from_dict(q).doc_type(Post).sort({"created_at": {"order": "desc"}}).execute()

    return [p for p in response.hits]