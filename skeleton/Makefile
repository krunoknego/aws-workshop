export AWS_REGION ?= eu-central-1
export PWD ?= $(shell pwd)

default: help

cli: ## Setup: enter the cli of the python container
	docker-compose exec -it aws-workshop-python bash -c "cd project && bash"
.PHONY: cli

root-cli: ## Setup: enter the cli of the python container as root user
	docker-compose exec --user root aws-workshop-python bash
.PHONY: root-cli

start: ## Setup: start containers
	docker-compose up -d
.PHONY: start

recreate: ## Setup: recreate containers
	docker-compose up -d --build --force-recreate
.PHONY: recreate

stop: ## Setup: stop containers
	docker-compose stop
.PHONY: stop

down: ## Setup: remove containers
	docker-compose down
.PHONY: down

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":[^:]*?## "}; {printf "\033[38;5;69m%-30s\033[38;5;38m %s\033[0m\n", $$1, $$2}'
.PHONY: help
