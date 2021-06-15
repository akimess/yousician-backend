import json
from api.v1.database.models import Song
from mongoengine.queryset.visitor import Q
from statistics import mean

class SongService:

    def get_all_songs(self, pageNumber, pageSize):
        offset = (pageNumber - 1) * pageSize
        songs = Song.objects.skip(offset).limit(pageSize)
        return json.loads(songs.to_json()), 200
    
    def get_average_difficulty(self, level):
        difficulty = None
        if level is None:
            difficulty = Song.objects.average('difficulty')
        else:
            difficulty = Song.objects(level=level).average('difficulty')
        return {"average": difficulty}, 200
    
    def find_song(self, keyword):
        songs = Song.objects(Q(artist__icontains=keyword) | Q(title__icontains=keyword))
        return json.loads(songs.to_json()), 200
    
    def get_ratings(self, id):
        song = Song.objects.get(id=id)
        rating = song['rating']
        if len(rating) == 0:
            return {"message": "No ratings available."}, 200
        else:
            return {
                "average": mean(rating),
                "lowest": min(rating),
                "highest": max(rating)
            }, 200
    
    def put_rating(self, id, rating):
        if isinstance(rating, int) and 0 < rating <= 5:
            song = Song.objects.get(id=id).update(add_to_set__rating=int(rating))
            return {"message": "Update was successfull"}, 200
        else:
            return {"message": "Rating should be an integer and between 1 and 5."}, 400
        