from fastapi import FastAPI
import datetime
import logging
from pydantic import BaseModel


class HelloWorldResponse(BaseModel):
    message: str


class ParrotRequestParams(BaseModel):
    n_repeat: int
    sep: str
    parrot_str: str


class ParrotRequest(BaseModel):
    header: str
    parrot_request: ParrotRequestParams


class ParrotBackResponseResults(BaseModel):
    time: str
    parrot: str


class ParrotBackResponse(BaseModel):
    header: str
    results: ParrotBackResponseResults


def create_app():
    app = FastAPI()

    @app.get("/hello_world", response_model=HelloWorldResponse)
    async def hello_world():
        logging.debug('/hello_world')
        return {"message": "Hello World"}

    @app.post("/parrot_back", response_model=ParrotBackResponse)
    async def parrot_back(p: ParrotRequest):
        p_dict = p.dict()
        logging.debug('/parrot_back: '+str(p_dict))
        params = p_dict['parrot_request']
        r_dict = {'header': p_dict['header'],
                  'results': {'time': datetime.datetime.utcnow().isoformat(timespec='seconds')+'Z',
                              'parrot': 'parrot back ' + params['sep'].join([params['parrot_str']]*params['n_repeat'])
                              }
                  }
        return r_dict

    return app

app = create_app()
