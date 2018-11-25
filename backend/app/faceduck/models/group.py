from elasticsearch_dsl import Document, Date, Text, Keyword, InnerDoc, Nested, Integer
from faceduck.models.post import Post
from faceduck.models.user import User

class Group(Document):
    name = Text()
    image_url = Text()
    admins = Text(multi=True)
    users = Text(multi=True) #Users + Admins
    posts = Text(multi=True)
    class Index:
        name = 'group'

    def save(self, ** kwargs):
        return super().save(** kwargs)

    def makeAdmin(self,user_id):
        if user_id not in self.admins:
            self.admins.append(user_id)

    def addUser(self,user):
        if user.meta.id not in self.users:
            self.users.append(user.meta.id)
            user.addGroup(self.meta.id)
            user.save()


    def isAdmin(self, user_id):
        if user_id in self.admins:
            return True
        return False

    def isUser(self, user_id):
        if user_id in self.users:
            return True
        return False

    def removeUser(self,user):
        if user.meta.id in self.users:
            self.users.remove(user.meta.id)
        if user.meta.id in self.admins:
            self.admins.remove(user.meta.id)
        user.removeGroup(self.meta.id)
        user.save()

    def makeUser(self,user_id):
        if user_id in self.admins:
            self.admins.remove(user_id)

    def getUsers(self):
        return self.users

    def getAdmins(self):
        return self.admins

    def addPost(self, post_id):
        self.posts.append(post_id)

    def removePost(self,post_id):
        for post in self.posts:
            if post == post_id:
                self.posts.remove(post)

    def getPosts(self):
        return self.posts