# fastapi_play
a repo for playing with FastAPI and Docker

### FastAPI app ###

The app is contained wholely in the 'api' directory.

A development environment can be created with `uv`
```
# in fastapi_play/api/
uv sync --locked
```
or, in the absence of `uv`, after creating a suitable environment,
```
# in fastapi_play/api/
pip install -r github-pipeline-requirements.txt
```

The unit tests can be run using pytest (from the api directory).
```
# in fastapi_play/api/
python -m pytest
```

The app can be brought up in a development server by running
```
# in fastapi_play/api/
python asgi.py
```

### Docker ###

The docker setup consists of:

*  docker-compose.yml
*  Dockerfile.uvicorn
*  Dockerfile.granian

Unit tests and builds can be run using
```
# in fastapi_play/
docker compose build
```
and the app can be run (in a container) using
```
# in fastapi_play/
docker compose up
```

The available server ports cat be obtained from
```
docker container ps
```

### FastAPI docs ###

Once the app is running, one can interact directly with the endpoints. As for all FastAPI apps, there are docs available on the endpoints
*  /openapi.json
*  /docs
*  /redoc