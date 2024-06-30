# Web_sever
In this repository, I simulate two hosts, a client and a server, where the server hosts a docker container in which it runs a web server, and the client hosts a docker container which inside runs a client that queries the web server. To run the script, first of all, we have to run the clean.sh file, which helps to clear the mininet network and also to clear the containers existing. Then finally, we build the docker images using the build_docker_images.sh file. Then when the images are built, the Topology.py file is run. As the topology runs, the client queries the web server to generate a web page, and the client queries the web server 10 times.

As the client queries the web server, a TCP dump is performed at the client side to capture the packets as they move between the client and the server, which are then stored in a pcap file, which is stored into the pcap folder.

## Steps to Run the Simulation

1. **Run the `clean.sh` file**
   ```bash
   ./clean.sh

2. **Run the `build_docker_images.sh` file**
   ```bash
   /build_docker_images.sh

3. **Run the `Topology.py` file**
   ```bash
   sudo python3 Topology.py

**Sample pcap file for the traffic captured during the browsing of the web server**

![Alt text](https://github.com/johnsengendo/Web_sever/blob/main/Screenshot%202024-07-01%20003211.png)


