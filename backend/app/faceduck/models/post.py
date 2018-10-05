from elasticsearch_dsl import Document, Date, Nested, Boolean, Text, Integer, InnerDoc

class Post(Document):
	text = Text()
	created_at = Date()
	author = User()

	class Index:
		name = 'post'

	def save(self, ** kwargs):
        return super().save(** kwargs)