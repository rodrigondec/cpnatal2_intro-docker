################################################################################
# Docker service commands
################################################################################
build:
	docker build . -t cpnatal2_intro-docker_requester

run:
	docker run -e "HOST_URL=server" cpnatal2_intro-docker_requester

run.link:
	docker run -e "HOST_URL=server" --link server cpnatal2_intro-docker_requester

containers.stop:
	docker stop $(docker ps -aq)

containers.remove:
	docker rm $(docker ps -aq)

images.remove:
	docker rmi $(docker images -q)