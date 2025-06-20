# command to build docker images
docker build -t <nameofdockerimage> .

# command to remove docker images
docker rmi <dockerid>
docker rmi image <imagename>

# single command to remove all docker images
docker rmi -f $(docker images -aq)

# dangerous docker command
docker images prune

# command to build a container image
docker run --name gold-container -dp 5001:5001 gold

# command to stop a container from running
docker stop <image id>

# To remove all containers
docker rm -vf $(docker ps -a -q)

# list of docker commands
docker --help

# command to exec into a running container
docker exec -it <nameofcontainer> sh

# command to see running container
docker ps

# command to see both stopped and running containers
docker ps -a

# command to start & stop a container
docker start <imageID>
docker stop <imageID>