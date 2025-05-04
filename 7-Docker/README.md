# Docker Commands
docker images

# start a container from an Image?
Image - A snapshot of our environment (code + dependencies)

Container - A running instance of an image

Dockerfile - Text file instructions to build a docker image

Dockerhub - public repositoty for Dockier Images


# Pull an image
docker pull image_name: tag

# Start the container from the image
docker run --name test_image -d -p 8080:80 nginx:latest

#buiding Docker Images
docker build -n demo_image .
docker run -p 7860:7860 docker_demo

# Login with Dockerhub
# Rename the Docker image 
docker tag <old_name> <docker-user-id/new-name>
docker push <docker-user-id/new-name>