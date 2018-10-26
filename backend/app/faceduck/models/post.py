from elasticsearch_dsl import Document, Date, Text, InnerDoc,Nested, Object

class Reaction(InnerDoc):
    user_id = Text()
    reaction = Text()

class Post(Document):
    text = Text()
    created_at = Date()
    author = Text()
    image_url = Text()
    user_reaction = Nested(Reaction)
    #reaction_count = Object()

    class Index:
        name = 'post'

    def save(self, ** kwargs):
        return super().save(** kwargs)

    def add_reaction(self,user_id, reaction):
        self.user_reaction.append(
            Reaction(user_id=user_id, reaction=reaction)
        )
        #if reaction_count:
        #    reaction_count[reaction] += 1
        #else:
        #    reaction_count[reaction] = 1

