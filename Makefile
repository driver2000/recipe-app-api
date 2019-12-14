VERSION ?= latest
IMAGE_NAME ?= recipe-app

.PHONY: build requirements.txt

requirements.txt:
	poetry export -f requirements.txt --without-hashes > requirements.txt

build: Dockerfile requirements.txt
    docker build -t $(IMAGE_NAME):$(VERSION) -f Dockerfile .

default: build
