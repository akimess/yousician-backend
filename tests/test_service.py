import unittest
from mongoengine import connect, disconnect
from api.v1.resources.service import SongService
from api.v1.database.models import Song
from statistics import mean

class SongServiceTestCase(unittest.TestCase):

    @classmethod
    def tearDown(cls):
        disconnect()
    
    def test_get_all_songs(self):
        connect('mongoenginetest', host='mongomock://localhost')
        data = {"artist": "The Yousicians","title": "Lycanthropic Metamorphosis","difficulty": 14.6,"level":13,"released": "2016-10-26"}
        song = Song(**data)
        song.save()

        song_service = SongService()
        songs, _ = song_service.get_all_songs(1,1)
        assert songs[0]['artist'] == 'The Yousicians'
    
    def test_get_average_difficulty(self):
        connect('mongoenginetest', host='mongomock://localhost')
        data1 = {"artist": "The Yousicians","title": "Lycanthropic Metamorphosis","difficulty": 14.6,"level":13,"released": "2016-10-26"}
        song1 = Song(**data1)
        song1.save()

        data2 = {"artist": "The Yousicians","title": "Lycanthropic Metamorphosis","difficulty": 5.6,"level":13,"released": "2016-10-26"}
        song2 = Song(**data2)
        song2.save()

        song_service = SongService()
        average, _ = song_service.get_average_difficulty(13)
        assert average['average'] == (data1['difficulty'] + data2['difficulty'])/2
    
    def test_find_song(self):
        connect('mongoenginetest', host='mongomock://localhost')
        data = {"artist": "The Yousicians","title": "Lycanthropic Metamorphosis","difficulty": 14.6,"level":13,"released": "2016-10-26"}
        song = Song(**data)
        song.save()

        song_service = SongService()
        songs, _ = song_service.find_song('the')
        assert songs[0]['artist'] == 'The Yousicians'
    
    def test_get_ratings(self):
        connect('mongoenginetest', host='mongomock://localhost')
        data = {"rating": [1,5],"artist": "The Yousicians","title": "Lycanthropic Metamorphosis","difficulty": 14.6,"level":13,"released": "2016-10-26"}
        song = Song(**data)
        song.save()

        song_service = SongService()
        ratings, _ = song_service.get_ratings(song.id)
        assert ratings['average'] == mean(data['rating'])
        assert ratings['lowest'] == min(data['rating'])
        assert ratings['highest'] == max(data['rating'])
    
    def test_put_rating(self):
        connect('mongoenginetest', host='mongomock://localhost')
        data = {"rating": [],"artist": "The Yousicians","title": "Lycanthropic Metamorphosis","difficulty": 14.6,"level":13,"released": "2016-10-26"}
        song = Song(**data)
        song.save()

        song_service = SongService()
        response, _ = song_service.put_rating(song.id, 3)
        assert response['message'] == 'Update was successfull'
        new_song = Song.objects.get(id=song.id)
        assert len(new_song['rating']) > 0
        assert new_song['rating'][0] == 3
