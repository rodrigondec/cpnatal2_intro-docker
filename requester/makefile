################################################################################
# Docker service commands
################################################################################
build:
	docker build . -t cpnatal2_intro-docker_requester

run:
	docker run -e "HOST_URL=server" --link server:rnc_cpnatal3-docker_server rnc_cpnatal3-docker_requester

containers.stop:
	docker stop $(docker ps -aq)

containers.remove:
	docker rm $(docker ps -aq)

images.remove:
	docker rmi $(docker images -q)