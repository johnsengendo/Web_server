# Web_sever

In this repository, I simulate two hosts: a client and a server. In each host, a containerized application is run—a web server on the server host and a web client on the client host. 

To run the script, first of all, we need to run the `clean.sh` file, which helps clear the Mininet network and also remove any existing containers. Then, we build the Docker images using the `build_docker_images.sh` file. Once the images are built, the `Topology.py` file is run. As the topology runs, the client queries the web server to generate a web page. The client queries the web server 10 times.
The server folder contains a web server Python script, where in it an HTML web page is written and hosted on the server, which the client queries when they connect to the web server. Furthermore, the server folder contains the Dockerfile for the server, and an installation package file for installing necessary packages.

The client folder contains a web client Python file which is used to query the web server to generate the web page. Furthermore, it contains the Dockerfile for the client and an installation packages file to install the necessary packages.

As the client queries the web server, a TCP dump is performed at the client side to capture the packets as they move between the client and the server, which are then stored in a pcap file, which is stored into the pcap folder.

## Steps to Run the Simulation

1. **Run the `clean.sh` file**
   ```bash
   ./clean.sh

2. **Run the `build_docker_images.sh` file**
   ```bash
   ./build_docker_images.sh

3. **Run the `Topology.py` file**
   ```bash
   sudo python3 Topology.py

**Sample pcap file for the traffic captured during the browsing of the web server**

![Alt text](https://github.com/johnsengendo/Web_sever/blob/main/Screenshot%202024-07-01%20003211.png)


