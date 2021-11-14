#!/bin/bash -

set -e -u

self_dir=$(dirname $0)

# Create the required mount directories if they do not exist; do not error out
# if they do.  For instance: on a clean checkout, we do not expect the
# directory "logs" to exist.
#
# Even if Docker currently auto-creates non-existent volume directories, we
# want to be explicit about our directories.  While the likelihood of Docker's
# behaviour changing is low due to backward compatibility, this gives us the
# added advantage that we will be resilient to a potential external change.
mkdir -p ${self_dir}/docker/{logs,pkgs,envs}

USER_ID="$(id -u)"; GROUP_ID="$(id -g)"
export USER_ID GROUP_ID

docker-compose -f ${self_dir}/docker-compose.yml up --build
