#!/bin/bash
set -e -u
self_dir=$(dirname $0)
cd ${self_dir}
# allow conda activate to be run in shell
source /opt/conda/etc/profile.d/conda.sh 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
# book-keeping
# git log -1 1>> /logs/git_stdout.log 2>> /logs/git_stderr.log
conda --version 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
# update environment from code on mountpoint
conda env update -f environment.yml -n server_in_docker_env 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
# activate environment and run service
conda activate server_in_docker_env 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
python -m pytest --cov=./api --cov-report=term-missing 1>> /logs/pytest_stdout.log 2>> /logs/pytest_stderr.log
cd ./api
uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 --log-config log_config.ini --log-level debug 1>> /logs/api_stdout.log 2>>/logs/api_stderr.log
