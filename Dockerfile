FROM continuumio/miniconda3

WORKDIR /app
COPY ./api /app
ENTRYPOINT ["bash", "run_server_in_docker.sh"]