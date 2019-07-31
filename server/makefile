################################################################################
# Docker service commands
################################################################################
build:
	docker build . -t cpnatal2_intro-docker_server

run:
	docker run --name server cpnatal2_intro-docker_server

run.port:
	docker run --name server -p 8000:8000 cpnatal2_intro-docker_server

containers.stop:
	docker stop $(docker ps -aq)

containers.remove:
	docker rm $(docker ps -aq)

images.remove:
	docker rmi $(docker images -q)