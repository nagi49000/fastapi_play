import logging
from api.fastapi_app import create_app

app = create_app()
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
