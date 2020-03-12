import sys
import argparse
import uvicorn
import logging
from api.fastapi_app import create_app

app = create_app()


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

    logging.basicConfig(filename=d['log_file'],
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        level=logging.getLevelName(d['log_level'].upper()))
    return {k: d[k] for k in {'host', 'port', 'log_level'}}


if __name__ == "__main__":
    kwargs = get_run_kwargs(sys.argv[1:])
    uvicorn.run("api.server:app", **kwargs)
