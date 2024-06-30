# The 'mn -c' command clears the network.
sudo mn -c
# Here we stops all running Docker containers.
docker stop $(docker ps -aq)
# This command removes all stopped Docker containers.
docker container prune -f
