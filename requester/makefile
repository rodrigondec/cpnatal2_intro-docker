################################################################################
# Docker service commands
################################################################################
build:
	docker build . -t cpnatal2_intro-docker_requester

create:
	docker create --name requester -e "HOST_URL=server" cpnatal2_intro-docker_requester

create.link:
	docker create --name requester -e "HOST_URL=server" --link server cpnatal2_intro-docker_requester

start:
	docker start requester

stop:
	docker stop requester

remove.container: stop
	docker rm requester

run:
	docker run --name requester -e "HOST_URL=server" cpnatal2_intro-docker_requester

run.link:
	docker run --name requester -e "HOST_URL=server" --link server cpnatal2_intro-docker_requester

remove.image:
	docker rmi cpnatal2_intro-docker_requester