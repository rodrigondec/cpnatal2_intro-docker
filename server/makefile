################################################################################
# Docker service commands
################################################################################
build:
	docker build . -t cpnatal2_intro-docker_server

create:
	docker create --name server cpnatal2_intro-docker_server

create.port:
	docker create --name server -p 8000:8000 cpnatal2_intro-docker_server

start:
	docker start server

stop:
	docker stop server

remove.container: stop
	docker rm server

run:
	docker run --name server cpnatal2_intro-docker_server

run.port:
	docker run --name server -p 8000:8000 cpnatal2_intro-docker_server

remove.image:
	docker rmi cpnatal2_intro-docker_server