from faceduck.models.post import Post

def search_posts(query):
    response = Post.search().from_dict({
        "query": {
            "match": {
                "text": query,
            }
        }
    }).doc_type(Post).execute()


    return [d for d in response.hits]