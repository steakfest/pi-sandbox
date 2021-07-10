#!/bin/bash

server="${1:-rpi-3b-001}"
service="sdhw"
project_dir="sharp-display-hello-world"

# Copy All the files
ssh pi@rpi-3b-001 -- mkdir -p /home/pi/${project_dir}/
scp * pi@rpi-3b-001:/home/pi/${project_dir}/

# Setup Systemd Unit...
ssh pi@rpi-3b-001 -- sudo ln -s /home/pi/${project_dir}/${service}.service /etc/systemd/system/${service}.service
ssh pi@rpi-3b-001 -- sudo systemctl daemon-reload
ssh pi@rpi-3b-001 -- sudo systemctl restart ${service}
