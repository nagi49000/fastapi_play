# fastapi_play
a repo for playing with FastAPI and Docker

### FastAPI app ###

The app is contained wholely in the 'api' directory. This contains unit tests, and a full environment.yml for a conda environment.

As a service, the service has two parts; the app and server. The app is written on top of FastAPI, and is unit tested. The server us uvicorn, which can be called at the command line, as in run_server.sh.

The unit tests can be run using pytest (from the api directory), and the server can be run using the shell script run_server.sh (from the api directory). For running thests and servers from other locations, add the api directory location to your PYTHONPATH.

### Docker ###

The docker setup consists of:

*  run-docker.sh
*  docker-compose.yml
*  Dockerfile
*  api\run_server_in_docker.sh

The docker set up may be run from the root directory using run-docker.sh. This configures the local mount directories, the user that is used within the Docker container (and is inherited from the current user), and runs the docker-compose.yml.

The docker-compose file runs the image build (as specified in the Dockerfile), and then runs the image. The image is run with a number of local mountpoints, environment variables etc., and finally a command is run, which is api\run_server_in_docker.sh.

run_server_in_docker.sh sets up the conda environment, and runs the uvicorn server.

In order to run the docker set up, you will need to be on a Linux box, with docker (CE will suffice) and docker-compose installed, and the user will need to be a part of the 'docker' group on the system.
