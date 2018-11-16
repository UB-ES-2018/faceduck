from elasticsearch_dsl import Document, Date, Text, Keyword, InnerDoc, Nested, Integer
from faceduck.models.post import Post
from faceduck.models.user import User

class Group(Document):
    name = Text()
    image_url = Text()
    admins = Keyword(multi=True)
    users = Keyword(multi=True) #Users + Admins
    posts = Nested(Post)
    class Index:
        name = 'group'

    def save(self, ** kwargs):
        return super().save(** kwargs)

    def makeAdmin(self,user_id):
        if user_id not in self.admins:
            self.admins.append(user_id)

    def addUser(self,user):
        if user.meta.user_id not in self.users:
            self.users.append(user.meta.user_id)
            user.addGroup(self.meta.id)


    def isAdmin(self, user_id):
        if user_id in self.admins:
            return True
        return False

    def isUser(self, user_id):
        if user_id in self.users:
            return True
        return False

    def removeUser(self,user_id):
        if user_id in self.users:
            self.users.remove(user_id)
        if user_id in self.admins:
            self.admins.remove(user_id)
        user.removeGroup(self.meta.id)
    
    def makeUser(self,user_id):
        if user_id in self.admins:
            self.admins.remove(user_id)

    def getUsers(self):
        return self.users

    def getAdmins(self):
        return self.admins

    def addPost(self, post):
        self.posts.append(post)

    def removePost(self,post_id):
        for post in self.posts:
            if post.meta.id == post_id:
                self.posts.remove(post)
                post.remove()

    def getPosts(self):
        return self.posts