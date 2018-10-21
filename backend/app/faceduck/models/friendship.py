from elasticsearch_dsl import Document, Date, Nested, Boolean, Text, Integer, InnerDoc


class Friendship(Document):
    user_id = Text()
    target_id = Text()
    
    state = Text() #'friends', 'not-friends', 'pending'

    class Index:
        name = 'friendship'
    
    def save(self, ** kwargs):
        return super().save(** kwargs)

