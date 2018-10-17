from faceduck.models.user import User


def search_users(query):
    response = User.search().from_dict({
        "query": {
            "multi_match": {
                "query": query,
                "type": "phrase_prefix",
                "fields": ["username", "name", "surname"]
            }
        }
    }).doc_type(User).execute()

    return [d for d in response.hits]

