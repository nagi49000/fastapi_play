import time
import sys
import argparse
import uvicorn
import logging
from api.fastapi_app import create_app


def get_run_kwargs(command_line_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1', type=str, help='URL for the server')
    parser.add_argument('--port', default=8000, type=int, help='port number for the server')
    parser.add_argument('--log-file', default=None, type=str, help='file to write logging into')
    parser.add_argument('--log-level', default='debug', type=str,
                        choices=['critical', 'error', 'warning', 'info', 'debug'],
                        help='level for logging in critical, error, warning, info, debug, trace')
    args = parser.parse_args(command_line_args)
    d = vars(args)

    #logging.basicConfig(filename=d['log_file'],
    #                    format='%(asctime)s %(levelname)-8s %(message)s',
    #                    level=logging.getLevelName(d['log_level'].upper()))

    run_kwargs = {k: d[k] for k in {'host', 'port', 'log_level'}}
    run_kwargs['log_config'] = get_log_config(logging.getLevelName(d['log_level'].upper()))
    return run_kwargs

def get_log_config(debug_level):
    d = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
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
        "": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
    },
}
    return d
    
app = create_app()


if __name__ == "__main__":
    kwargs = get_run_kwargs(sys.argv[1:])
    uvicorn.run("api.server:app", **kwargs)
