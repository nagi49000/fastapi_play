cd ./api
uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 --log-config log_config.ini
