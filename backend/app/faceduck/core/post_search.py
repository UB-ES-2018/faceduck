from faceduck.models.post import Post

START = 0
SIZE = 50


def search_posts(query, start=START, size=SIZE):
    response = Post.search().from_dict({
        "query": {
            "match": {
                "text": query,
            }
        }
    }).doc_type(Post).sort({"created_at": {"order": "desc"}})[start:size].execute()


    return [d for d in response.hits]


def search_posts_by_author(author, start=START, size=SIZE):
    response = Post.search().from_dict({
        "query": {
            "match_phrase": {
                "author": author
            }
        }
    }).doc_type(Post).sort({"created_at": {"order": "desc"}})[start:size].execute()
    
    return [d for d in response.hits]

def search_posts_by_tag(tag):
    response = Post.search().from_dict({
        "query": {
            "match_phrase":{
                "tags" : tag
            } 
        }
    }).doc_type(Post).execute()

    return [d for d in response.hits]
