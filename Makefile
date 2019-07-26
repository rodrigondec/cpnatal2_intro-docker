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

clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop
