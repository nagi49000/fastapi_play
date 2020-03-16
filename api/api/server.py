import time
import sys
import argparse
import uvicorn
import logging
from api.fastapi_app import create_app


def get_run_kwargs(command_line_args):
    """ command_line_args - list<str> - list of args as supplied fy sys.argv

        returns a dict to initialise uvicorn.run
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1', type=str, help='URL for the server')
    parser.add_argument('--port', default=8000, type=int, help='port number for the server')
    parser.add_argument('--log-file', default=None, type=str, help='file to write logging into')
    parser.add_argument('--log-level', default='debug', type=str,
                        choices=['critical', 'error', 'warning', 'info', 'debug'],
                        help='level for logging in critical, error, warning, info, debug, trace')
    args = parser.parse_args(command_line_args)
    d = vars(args)

    run_kwargs = {k: d[k] for k in {'host', 'port'}}
    run_kwargs['log_config'] = get_log_config(logging.getLevelName(d['log_level'].upper()))
    return run_kwargs


def get_log_config(log_level):
    """ log_level - str - legitimate logging level string

        returns a dict representing the level config. Bit of a
        monster, since a full uvicorn logging config...
    """
    d = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(asctime)s %(levelname)-8s %(message)s",
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "access": {
                "formatter": "access",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "": {"handlers": ["default"], "level": log_level},
            "uvicorn.error": {"level": log_level},
            "uvicorn.access": {"handlers": ["access"], "level": log_level, "propagate": False},
        },
    }
    return d


app = create_app()


if __name__ == "__main__":
    kwargs = get_run_kwargs(sys.argv[1:])
    uvicorn.run("api.server:app", **kwargs)
