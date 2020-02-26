APP_NAME = SurveyDonkey
APP_VERSION ?= v1
SERVICE_NAME = poll
APP_ENVIRONMENT ?= dev


#Export Variables into child processes
.EXPORT_ALL_VARIABLES:

database:
	docker-compose up -d database
.PHONY: database

db_migrate:
	docker-compose run flyway migrate
.PHONY: db_migrate

db_clean:
	docker-compose run flyway clean
.PHONY: db_clean

build: .env
	docker-compose run --rm python bash cicd/scripts/build.sh
.PHONY: build

deploy:
	bash cicd/scripts/deploy.sh
.PHONY: deploy

deploy_api:
	bash cicd/scripts/deploy_api.sh
.PHONY: deploy_api

clean:
	docker-compose down --remove-orphans
	bash cicd/scripts/clean.sh
.PHONY: clean

# create .env with .env.template if it doesn't exist already
.env:
	cp .env.template .env