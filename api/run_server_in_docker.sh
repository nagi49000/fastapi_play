#!/bin/bash
self_dir=$(dirname $0)
cd ${self_dir}
# allow conda activate to be run in shell
source /opt/conda/etc/profile.d/conda.sh 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
# book-keeping
conda --version 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
# update environment from code on mountpoint
conda env update -f environment.yml -n server_in_docker_env 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
# activate environment and run service
conda activate server_in_docker_env 1>> /logs/conda_stdout.log 2>>/logs/conda_stderr.log
python api/server.py --host 0.0.0.0 --port 8000 1>> /logs/api_stdout.log 2>>/logs/api_stderr.log
