#!/bin/bash
cd /api
conda env update -f /api/environment.yml -n server_in_docker_env 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
conda run -n server_in_docker_env python api/server.py --host 0.0.0.0 --port 8000 1>> /logs/api_stdout.log 2>>/logs/api_stderr.log
