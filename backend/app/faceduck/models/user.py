from elasticsearch_dsl import Document, Date, Nested, Boolean, Text, Integer, InnerDoc, Keyword


class LoginLog(InnerDoc):
    ip = Text()
    device = Text()
    date = Date()
    state = Boolean()

class User(Document):
    username = Text()
    email = Text()
    password = Text()
    
    name = Text()
    surname = Text()
    birthday = Date()
    gender = Text()

    login_logs = Nested(LoginLog)
    
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
    
    def add_log(self, device, ip, state, date):
        entry = LoginLog(device=device, ip=ip, state=state, date=date)
        self.login_logs.append(entry)
        return entry

    def get_login_logs(self):
        return self.login_logs
    
    def addGroup(self,group_id):
        if group_id not in self.groups:
            self.groups.append(group_id)

    def removeGroup(self, group_id):
        if group_id in self.groups:
            self.groups.remove(group_id)

