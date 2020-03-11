FROM continuumio/miniconda3

WORKDIR /app
COPY ./api /app
RUN conda env create -f /app/environment.yml -n webenv

ENTRYPOINT ["conda", "run", "-n", "webenv", "python", "api/server.py", "--host", "0.0.0.0", "--port", "8000", "--log-file", "/logs/api.log"]