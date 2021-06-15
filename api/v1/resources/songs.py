import json
from flask import abort, request
from flask_restx import Namespace, Resource, reqparse
from api.v1.resources.service import SongService

songs = Namespace('v1/songs', description='Songs namespace')

song_service = SongService()

pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument(
    "pageNumber", type=int, required=False, default=1, help="Page Number"
)
pagination_parser.add_argument(
    "pageSize", type=int, required=False, default=20, help="Page size"
)

''' A: Return a list of all songs. '''
@songs.route('/')
class SongsApi(Resource):
    def get(self):
        p_args = pagination_parser.parse_args()
        page_nb = p_args.get("pageNumber")
        items_per_page = p_args.get("pageSize")
        return song_service.get_all_songs(page_nb, items_per_page)

''' B: return the average difficulty for all songs.'''
@songs.route('/difficulty', defaults={'level': None})
@songs.route('/difficulty/<level>')
class SongsApi(Resource):
    def get(self, level):
        return song_service.get_average_difficulty(level)

''' C: returns a list of songs matching the string '''
@songs.route('/search/<message>')
class SongsApi(Resource):
    def get(self, message):
        return song_service.find_song(message)

''' D: add a rating for a given song '''
''' E: returns the average, the lowest and the highest rating'''
@songs.route('/rating/<id>')
class SongsApi(Resource):
    def get(self, id):
        return song_service.get_ratings(id)

    def put(self, id):
        rating = request.form['rating']
        return song_service.put_rating(id, rating)

        

