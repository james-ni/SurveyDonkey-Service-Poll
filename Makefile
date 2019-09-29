APP_NAME = ServerlessDemo
SERVICE_VERSION ?= v1
SERVICE_NAME = Poll
APP_ENVIRONMENT ?= dev

#Export Variables into child processes
.EXPORT_ALL_VARIABLES:



build:
	bash cicd/scripts/build.sh
.PHONY: build


deploy:
	bash cicd/scripts/deploy.sh
.PHONY: deploy


clean:
	bash cicd/scripts/clean.sh
.PHONY: clean
