run:
	docker run --name server -p 8000:8000 rnc_cpnatal3-docker_server

containers.stop:
	docker stop $(docker ps -aq)

containers.remove:
	docker rm $(docker ps -aq)

images.remove:
	docker rmi $(docker images -q)