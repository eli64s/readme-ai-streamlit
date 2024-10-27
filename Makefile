SHELL := /bin/bash
SRC_PATH := readmeai
TEST_PATH := tests

.PHONY: clean
clean: ## Remove project build artifacts
	./scripts/clean.sh clean

.PHONY: format
format: ## Format codebase using Ruff
	ruff format .

.PHONY: lint
lint: ## Lint codebase using Ruff
	ruff check . --fix

.PHONY: run-app
run-app: ## Run Streamlit app locally
	streamlit run src/app.py

.PHONY: test
test: ## Run unit test suite
	pytest

.PHONY: help
help: Makefile ## Display the help menu
	@echo -e ""
	@echo -e "Usage: make [target]"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo -e "__________________________________________________________________________________________\n"
