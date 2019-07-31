################################################################################
# Docker-compose service commands
################################################################################
build:
	docker-compose build

up: build
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

containers.stop:
	docker stop $(docker ps -aq)

containers.remove:
	docker rm $(docker ps -aq)

images.remove:
	docker rmi $(docker images -q)
