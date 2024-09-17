# Web_server

In this repository, I simulate two hosts: a client and a server. In each host, a containerized application is run—a web server on the server host and a web client on the client host. 

To run the script, first of all, we need to run the `clean.sh` file, which helps clear the Mininet network and also remove any existing containers. Then, we build the Docker images using the `build_docker_images.sh` file. Once the images are built, the `Topology.py` file is run. As the topology runs, the client queries the web server to generate a web page, a pcap file of the traffic is further captured at the client side. The client queries the web server 10 times to retreive the webpage at the server.

## Folders description

- **Server folder contains:**
  - The web server python file
  - The Dockerfile for the server
  - An installation script for the necessary packages

- **Client folder contains:**
  - The web client python file.
  - The Dockerfile for the client
  - An installation file for the necessary packages

- **pcap folder:**
  - Stores the generated pcap files

- **Image folder:**
  - Stores necessary images.


## Steps to run the topology

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


