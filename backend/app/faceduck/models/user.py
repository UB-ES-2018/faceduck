from elasticsearch_dsl import Document, Date, Nested, Boolean, Text, Integer, InnerDoc, Keyword


class User(Document):
    username = Text()
    email = Text()
    password = Text()
    
    name = Text()
    surname = Text()
    birthday = Date()
    gender = Text()
    
    groups = Keyword(multi = True)
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

    def addGroup(self,group_id):
        if group_id not in self.groups:
            self.groups.append(group_id)

    def removeGroup(self, group_id):
        if group_id in self.groups:
            self.groups.remove(group_id)

