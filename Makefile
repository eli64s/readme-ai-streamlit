# Makefile

SHELL := /bin/bash
VENV := readmeai

.PHONY: help clean format lint conda-recipe git-rm-cache test poetry-reqs word-search

help:
	@echo "Commands:"
	@echo "clean        : repository file cleanup."
	@echo "format       : executes code formatting."
	@echo "lint         : executes code linting."
	@echo "conda-recipe : builds conda package."
	@echo "git-rm-cache : fix git untracked files."
	@ech "run		    : runs the application."
	@echo "test         : executes tests."
	@echo "poetry-reqs  : generates requirements.txt file."
	@echo "word-search  : searches for a word in the repository."

.PHONY: clean
clean: format lint
	./scripts/clean.sh clean

.PHONY: format
format:
	@echo -e "\nFormatting in directory: ${CURDIR}"
	ruff format .

.PHONY: lint
lint:
	@echo -e "\nLinting in directory: ${CURDIR}"
	ruff check . --fix


.PHONY: conda-recipe
conda-recipe:
	grayskull pypi readmeai
	conda build .

.PHONY: git-rm-cache
git-rm-cache:
	git rm -r --cached .

.PHONY: run
run:
	python -m streamlit run src/app.py

.PHONY: test
test:
	pytest \
	-n auto \
	--cov=./ \
	--cov-report=xml \
	--cov-report=term-missing \
	--cov-branch

.PHONY: poetry-reqs
poetry-reqs:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: word-search
word-search: clean
	@echo -e "\nSearching for: ${WORD} in directory: ${CURDIR}"
	grep -Ril ${WORD} readmeai tests
