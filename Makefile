.PHONY: help clean clean-build clean-test clean-pyc lint test test-all coverage dist release install update versions docs
.SILENT: help versions
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys
from urllib.request import pathname2url
webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
print("\n* Run `brew install sed grep` for GNU tools on MacOS")
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"
SED=sed

ifeq ($(shell uname), Darwin)
	SED=gsed
endif

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -rf build/ dist/ .eggs/ site/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-test: ## remove test and coverage artifacts
	rm -rf .tox/ .pytest_cache
	rm -rf htmlcov/ .coverage coverage.json

lint: ## check pre-commit linting rules
	pre-commit run --all-files --show-diff-on-failure --color always

test: ## run tests quickly with the default Python
	python -m pytest --cov --cov-report=term --cov-report=html --no-cov-on-fail

test-all: ## run tests on every Python version with tox
	tox

coverage: test ## check code coverage quickly with the default Python
	coverage report
	$(BROWSER) htmlcov/index.html

dist: clean ## builds source and wheel package
	flit build
	ls -lh dist

release: clean ## package and upload a release
	flit publish
	ls -lh dist

install: clean ## install the package to the active Python's site-packages
	flit install --symlink

update: ## update all listed packages
	pip install -U -r requirements.dev.txt
	pip freeze --all --exclude-editable --exclude hue-api > requirements.txt

versions: ## show installed versions of listed packages
	pip freeze -r requirements.dev.txt | $(SED) '/The following requirements were added by pip freeze/Q'

docs: ## builds docs
	mkdocs build
	typer hue.cli utils docs --output docs/cli.md --name hue
