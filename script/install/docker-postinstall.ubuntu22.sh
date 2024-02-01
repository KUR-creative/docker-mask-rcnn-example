#!/bin/bash

## Use docker without sudo
sudo groupadd docker
sudo usermod -aG docker $USER

# Log out and Log back in so that your group membership is re-evaluated

# Verify
newgrp docker
docker run hello-world

## Run on boot
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

## Configure log rotation
CONTENT='{
 "log-driver": "json-file",
 "log-opts": {
    "max-size": "10m",
    "max-file": "3"
 }
}'

# TODO: Check existence first!
#echo "$CONTENT" | sudo tee /etc/docker/daemon.json
