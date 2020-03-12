FROM continuumio/miniconda3

WORKDIR /app
COPY ./api /app
RUN conda env update -f /app/environment.yml -n base
# RUN ls /logs

ENTRYPOINT ["python", "api/server.py", "--host", "0.0.0.0", "--port", "8000", "--log-file", "/logs/api.log"]