from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ReferenceField, EmbeddedDocumentField, ListField, StringField


class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description  = StringField()

class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors)
    quote = StringField()
