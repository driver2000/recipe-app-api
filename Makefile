VERSION ?= latest
IMAGE_NAME ?= recipe-app

.PHONY: build requirements

requirements.txt:
	poetry run pip freeze > requirements.txt

build: Dockerfile .requirements
    docker build -t $(IMAGE_NAME):$(VERSION) -f Dockerfile .

default: build
