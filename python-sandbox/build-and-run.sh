#!/bin/bash -e


set +e
docker buildx create --driver docker-container --name python-sandbox
docker buildx use python-sandbox
set -e

docker buildx build --load \
--platform linux/arm/v7,linux/arm64/v8,linux/amd64 \
--tag python-sandbox .

docker run -it --rm python-sandbox