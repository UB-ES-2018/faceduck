from elasticsearch_dsl import Document, Date, Text, InnerDoc,Nested, Integer

class Reaction(InnerDoc):
    user_id = Text()
    reaction = Text()

class ReactionCount(InnerDoc):
    reaction = Text()
    count = Integer()

class Post(Document):
    text = Text()
    created_at = Date()
    author = Text()
    image_url = Text()
    user_reaction = Nested(Reaction)
    reactions_count = Nested(ReactionCount)

    class Index:
        name = 'post'

    def save(self, ** kwargs):
        return super().save(** kwargs)

    def add_reaction(self,user_id, reaction):
        self.user_reaction.append(
            Reaction(user_id=user_id, reaction=reaction)
        )

        found = False
        for rc in self.reactions_count:
            if rc.reaction == reaction:
                rc.count += 1
                found = True
        if not found:
            self.reactions_count.append(ReactionCount(reaction=reaction,count=1))


    def update_reaction(self, user_id, reaction):
        for r in self.user_reaction:
            if r.user_id == user_id:
                old_reaction = r.reaction
                r.reaction = reaction

        found = False
        for rc in self.reactions_count:
            if rc.reaction == old_reaction:
                rc.count -= 1
                if rc.count == 0:
                    self.reactions_count.remove(rc)
            if rc.reaction == reaction:
                rc.count += 1
                found = True
        if not found:
            self.reactions_count.append(ReactionCount(reaction=reaction,count=1))

    def remove_reaction(self,user_id):
        reaction = ""
        for r in self.user_reaction:
            if r.user_id == user_id:
                reaction = r.reaction
                self.user_reaction.remove(r)

        for rc in self.reactions_count:
            if rc.reaction == reaction:
                rc.count -= 1
                if rc.count == 0:
                    self.reactions_count.remove(rc)
