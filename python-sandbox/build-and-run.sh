#!/bin/bash -e


set +e
docker buildx create --driver docker-container --name python-sandbox
docker buildx use python-sandbox
set -e

docker buildx build --push \
--platform linux/arm/v7,linux/arm64/v8,linux/amd64 \
--tag ghcr.io/steakfest/python-sandbox:latest .

docker run -it --rm ghcr.io/steakfest/python-sandbox:latest