from elasticsearch_dsl import Document, Date, Text


class Post(Document):
        text = Text()
        created_at = Date()
        author = Text()
        image_url = Text()
        tags = []

        class Index:
                name = 'post'

        def save(self, ** kwargs):
                return super().save(** kwargs)
