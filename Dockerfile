FROM continuumio/miniconda3:latest as builder

ENV APP_HOME=/app
WORKDIR ${APP_HOME}
COPY api ./

FROM builder AS tester
RUN conda env update --file environment-test.yml --name base --prune && \
    python -m pytest --cov=./api

FROM builder AS prod
RUN conda env update --file environment-prod.yml --name base --prune && \
    groupadd --system app && \
    useradd -g app --system app && \
    chown -R app:app ${APP_HOME} && \
    chmod -R 755 ${APP_HOME}
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "api.api_app:app", "--bind", "0.0.0.0:6780", "--log-level", "DEBUG"]