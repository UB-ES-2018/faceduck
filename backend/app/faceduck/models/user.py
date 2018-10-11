from elasticsearch_dsl import Document, Date, Nested, Boolean, Text, Integer, InnerDoc

class User(Document):
    username = Text()
    email = Text()
    password = Text()

    name = Text()
    surname = Text()
    birthday = Date()
    gender = Text()

    #location = Text()
    #description = Text()
    #url = Text()
    #registerDate = Date()
    #profileImagePath = Text()
    #phone = Text()
    #website = Text()
    #postCount = Integer()
    #posts = Nested(Post)
    #friendsCount = Integer()
    #friends = Nested(User)

    class Index:
        name = 'user'

    def save(self, ** kwargs):
        return super().save(** kwargs)