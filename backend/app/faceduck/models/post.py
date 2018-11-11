from elasticsearch_dsl import Document, Date, Text, InnerDoc,Nested, Integer
import sys
class Reaction(InnerDoc):
    user_id = Text()
    reaction = Text()

class ReactionCount(InnerDoc):
    reaction = Text()
    count = Integer()

class Comment(InnerDoc):
    user_id = Text()
    text = Text()
    comment_id = Integer()

class Post(Document):
    text = Text()
    created_at = Date()
    author = Text()
    image_url = Text()
    user_reaction = Nested(Reaction)
    reactions_count = Nested(ReactionCount)
    comments = Nested(Comment)
    comments_count = Integer()
    comments_id = Integer()

    class Index:
        name = 'post'

    def save(self, ** kwargs):
        if self.comments_id is None:
            self.comments_count = 0
            self.comments_id = 0
        return super().save(** kwargs)

    '''
    COMMENTS
    '''
    def add_comment(self, user_id, text):
        self.comments_id = self.comments_id + 1
        c = Comment(user_id = user_id, text=text,comment_id=self.comments_id)
        self.comments.append(c)
        self.comments_count += 1
        return c

    def get_comments(self):
        return self.comments

    def remove_comment(self, comment_id):
        for c in self.comments:
            print(comment_id, file=sys.stderr)
            if c.comment_id == comment_id:
                self.comments.remove(c)
                self.comments_count -= 1
    '''
    REACTIONS
    '''
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
