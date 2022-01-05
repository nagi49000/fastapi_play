# fastapi_play
a repo for playing with FastAPI and Docker

### FastAPI app ###

The app is contained wholely in the 'api' directory. This contains unit tests, and a full ymls for a conda environments (a -test.yml for dev, and a -prod.yml for prod).

The unit tests can be run using pytest (from the api directory).

The app can be brought up in a development server by running (in the api directory)
```
python asgi.py
```

### Docker ###

The docker setup consists of:

*  docker-compose.yml
*  Dockerfile-prod
*  Dockerfile-test

Unit tests and builds can be run using
```
docker-compose build
```
and the app can be run (in a container) using
```
docker-compose up
```

### FastAPI docs ###

Once the app is running, one can interact directly with the endpoints. As for all FastAPI apps, there are docs available on the endpoints
*  /openapi.json
*  /docs
*  /redoc