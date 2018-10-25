from elasticsearch_dsl import Document, Date, Text, Keyword


class Post(Document):
        text = Text()
        created_at = Date()
        author = Text()
        image_url = Text()
        tags = Keyword(multi=True)

        class Index:
                name = 'post'

        def save(self, ** kwargs):
                return super().save(** kwargs)
