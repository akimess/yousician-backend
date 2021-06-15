from api.v1.resources.songs import songs

def initialize_routes(api):
    api.add_namespace(songs)