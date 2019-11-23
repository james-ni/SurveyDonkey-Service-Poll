APP_NAME = SurveyDonkey
APP_VERSION ?= v1
SERVICE_NAME = poll
APP_ENVIRONMENT ?= dev


#Export Variables into child processes
.EXPORT_ALL_VARIABLES:

lint:
	echo helloworld
.PHONY: lint

build:
	bash cicd/scripts/build.sh
.PHONY: build


deploy:
	bash cicd/scripts/deploy.sh
.PHONY: deploy

deploy_api:
	bash cicd/scripts/deploy_api.sh
.PHONY: deploy_api

clean:
	bash cicd/scripts/clean.sh
.PHONY: clean
