from os import getenv
from .fastapi_app import create_app
app = create_app(logger_name=getenv("LOGGER_NAME", "gunicorn.error"))
