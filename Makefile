# Makefile for building and running the project in Docker

IMAGE_NAME=did-portability-poc

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm $(IMAGE_NAME)

clean:
	docker rmi $(IMAGE_NAME)
