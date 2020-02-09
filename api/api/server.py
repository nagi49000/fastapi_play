import logging
from api.fastapi_app import create_app

app = create_app()
logging.basicConfig(filename=None,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.DEBUG)
