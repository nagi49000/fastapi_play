FROM mambaorg/micromamba:latest as builder

ENV APP_HOME=/home/mambauser/app
# run mkdir so that folder owned by mambauser
RUN mkdir ${APP_HOME}
WORKDIR ${APP_HOME}
COPY --chown=mambauser:mambauser api ./
RUN micromamba update -f environment-prod.yml --name base

FROM builder AS tester
RUN micromamba install pytest-cov -c conda-forge --name base && \
    # for some reason, PATH not working here, so use full path
    /opt/conda/bin/python -m pytest --cov=./api

FROM builder AS prod
RUN micromamba clean
# switch to root briefly to make a specific user for app
USER root
RUN groupadd --system app && \
    useradd -g app --system app && \
    chown -R app:app ${APP_HOME} && \
    chmod -R 755 ${APP_HOME}
USER app
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "api.api_app:app", "--bind", "0.0.0.0:6780", "--log-level", "DEBUG"]