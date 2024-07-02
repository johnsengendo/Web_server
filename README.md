# Web_server

In this repository, I use COMNETSEMU to simulate two hosts: a client and a server. In each host, a containerized application is run—a web server on the server host and a web client on the client host. 

To run the script, first of all, we need to run the `clean.sh` file, which helps clear the Mininet network and also remove any existing containers. Then, we build the Docker images using the `build_docker_images.sh` file. Once the images are built, the `Topology.py` file is run. As the topology runs, the client queries the web server to generate a web page. The client queries the web server 10 times.

The server folder contains a Python script for the web server, which writes and hosts an HTML web page that the client queries when connecting to the web server. Additionally, the server folder contains the Dockerfile for the server and an installation package file for installing the necessary packages.

The client folder contains a Python script for the web client, which is used to query the web server to generate the web page. Furthermore, it contains the Dockerfile for the client and an installation package file to install the necessary packages.

As the client queries the web server, a TCP dump is performed on the client side to capture the packets as they move between the client and the server. These packets are then stored in a pcap file, which is saved in the pcap folder.

## Steps to run the simulation

1. **Run the `clean.sh` file**
   ```bash
   ./clean.sh

2. **Run the `build_docker_images.sh` file**
   ```bash
   ./build_docker_images.sh

3. **Run the `Topology.py` file**
   ```bash
   sudo python3 Topology.py

**NB: after the running of the script please use ctrl+c to return to the mininet CLI** <br>
Still fixing  this ....

**Sample pcap file for the traffic captured during the browsing of the web server**

![Alt text](https://github.com/johnsengendo/Web_sever/blob/main/Images/Screenshot%202024-07-01%20143046.png)


