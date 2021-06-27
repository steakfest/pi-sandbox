# FROM arm32v6/python:3

# WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD [ "python", "./hello-world.py" ]

ARG ARCH=
FROM ${ARCH}debian:buster-slim

RUN apt-get update \
&& apt-get install -y python3 \
&& rm -rf /var/lib/apt/lists/*

# ENTRYPOINT [ "curl" ]