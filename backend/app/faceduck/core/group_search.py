from faceduck.models.group import Group


def search_groups(query):
    response = Group.search().from_dict({
        "query": {
            "multi_match": {
                "query": query,
                "type": "phrase_prefix",
                "fields": ["name"]
            }
        }
    }).doc_type(Group).execute()

    return [d for d in response.hits]