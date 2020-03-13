FROM continuumio/miniconda3
WORKDIR /api
ENTRYPOINT ["bash", "run_server_in_docker.sh"]