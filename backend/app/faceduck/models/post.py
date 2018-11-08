from elasticsearch_dsl import Document, Date, Text, InnerDoc,Nested, Object,Integer

class Reaction(InnerDoc):
    user_id = Text()
    reaction = Text()

class Post(Document):
    text = Text()
    created_at = Date()
    author = Text()
    image_url = Text()
    user_reaction = Nested(Reaction)
    #reactions_count = Object()

    class Index:
        name = 'post'

    def save(self, ** kwargs):
        return super().save(** kwargs)

    def add_reaction(self,user_id, reaction):
        self.user_reaction.append(
            Reaction(user_id=user_id, reaction=reaction)
        )

    def update_reaction(self, user_id, reaction):
        for r in self.user_reaction:
            if r.user_id == user_id:
                r.reaction = reaction
                
    def remove_reaction(self,user_id):
        for r in self.user_reaction:
            if r.user_id == user_id:
                self.user_reaction.remove(r)
