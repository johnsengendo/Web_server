#!/bin/bash

# Updating package lists
apt-get update -y

# Installing useful tools
apt-get install -y --no-install-recommends \
    bash \
    python3 \
    python3-pip \
    bash-completion \
    curl \
    iproute2 \
    iputils-ping \
    net-tools
# Install Python packages
pip install requests

# Installing the packages required for streaming videos and dumping traffic.
apt-get install -y \
    tcpdump \
    nano

