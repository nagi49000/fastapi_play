export PYTHONPATH=${PYTHONPATH}:`pwd`
uvicorn api.server:app
