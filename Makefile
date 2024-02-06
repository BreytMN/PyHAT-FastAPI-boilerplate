PROJECT = pyhat_boilerplate

.PHONY: all help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

venv: ## Create virtual env
	@rm -rf .venv/ && python -m venv .venv && . .venv/bin/activate; \
	pip install --upgrade pip; \
	pip install \
		-r requirements.txt \
		-r requirements_dev.txt \
		-r requirements_test.txt

server-venv: ## Start server with venv in watch mode
	@cd app; \
	uvicorn main:app --reload

server-docker: ## Start server with docker
	@docker rm -f $(PROJECT) || true; \
	docker build . -t $(PROJECT); \
	docker run -it --name $(PROJECT) -p 8000:8000 $(PROJECT);

tests-unit: ## Run unit tests
	@clear && \
	python -m pytest \
		--cov-report=term-missing \
		--cov=app tests/unit/
