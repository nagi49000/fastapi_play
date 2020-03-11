import sys
import argparse
import uvicorn
import logging
from api.fastapi_app import create_app

app = create_app()


def get_run_kwargs(command_line_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='URL for the server', default='127.0.0.1', type=str)
    parser.add_argument('--port', help='port number for the server', default=8000, type=int)
    parser.add_argument('--log-file', help='file to write logging into', default=None, type=str)
    parser.add_argument(
        '--log-level', help='level for logging in critical, error, warning, info, debug, trace', default='debug', type=str)
    args = parser.parse_args(command_line_args)
    d = vars(args)

    logging.basicConfig(filename=d['log_file'],
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        level=logging.DEBUG)
    return {k: d[k] for k in {'host', 'port', 'log_level'}}


if __name__ == "__main__":
    kwargs = get_run_kwargs(sys.argv[1:])
    uvicorn.run("api.server:app", **kwargs)
