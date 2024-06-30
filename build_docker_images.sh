#!/bin/bash

echo "Building docker image for the web server"
docker build -t web_server --file ./Server/Dockerfile.server ./Server

echo "Building docker image for the web client"
docker build -t web_client --file ./Client/Dockerfile.client ./Client
