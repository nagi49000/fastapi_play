FROM continuumio/miniconda3
SHELL ["/bin/bash", "-c"]

WORKDIR /app
COPY ./api /app
RUN conda env create -f /app/environment.yml -n webenv

SHELL ["conda", "run", "-n", "webenv", "/bin/bash", "-c"]
ENTRYPOINT ["conda", "run", "-n", "webenv", "python", "api/server.py", "--host", "0.0.0.0", "--port", "8000"]