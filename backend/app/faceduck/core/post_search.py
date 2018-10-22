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


def search_posts_by_author(author):
    response = Post.search().from_dict({
        "query": {
            "match_phrase": {
                "author": author
            }
        }
    }).doc_type(Post).execute()
    
    return [d for d in response.hits]

def search_posts_by_tag(tag):
    response = Post.search().from_dict({
        "query": {
            "terms":{
                "tags" : tag
            } 
        }
    }).doc_type(Post).execute()

    return [d for d in response.hits]
