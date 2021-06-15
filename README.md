# Yousician-Backend

## How to run
```
docker-compose up
```
This will start a container for the backend and mongodb.  
After which you are able to visit "http://localhost:5100/" and view the Swagger API page.

## API endpoints  

### Get all songs with pagination
```
GET http://localhost:5100/v1/songs?pageNumber=X&pageSize=Y
```

### Get average difficulty
```
GET http://localhost:5100/v1/songs/difficulty/<level>
```
Level is an optional parameter.

### Search song by keyword
```
GET http://localhost:5100/v1/songs/search/<keyword>
```

### Add ratings to a song
```
PUT http://localhost:5100/v1/songs/rating/<id>
```
Request (form-data):
```
{
  "rating": X
}
```

### Get ratings
```
GET http://localhost:5100/v1/songs/rating/<id>
```

## Testing
Testing is done locally through venv.  
Commands to set it up:
```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install flask flask-restx Werkzeug mongoengine mongomock
```
Then to fire the tests, use:
```
python -m unittest tests/test_service.py
```

## Improvement
Several things I would have added or improved on:
1) Currently there are only unit tests. I would also have added integration tests.
2) More server side validation for input.
3) Additional test case scenarios for unit tests and not only positive ones.
4) Python testing with docker.
