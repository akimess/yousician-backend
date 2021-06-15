from mongoengine import Document, StringField, FloatField, ListField

class Song(Document):
    artist = StringField(required=True)
    title = StringField(required=True)
    difficulty = FloatField(required=True)
    level = FloatField(required=True)
    released = StringField(required=True)
    rating=ListField(required=False)