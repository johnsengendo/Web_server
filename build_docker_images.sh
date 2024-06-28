#!/bin/bash

echo "Build docker image for the video streaming server"
docker build -t video_streaming_server --file ./Server/Dockerfile.server ./Server

echo "Build docker image for the video streaming client"
docker build -t video_streaming_client --file ./Client/Dockerfile.client ./Client
