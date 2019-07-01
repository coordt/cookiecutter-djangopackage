.PHONY: clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

define ENSURE_MASTER_BRANCH_SCRIPT
BRANCH=$$(git rev-parse --abbrev-ref HEAD)
if [[ "$$BRANCH" != "master" ]]; then
  echo 'You can only release new versions when on the master branch.';
  exit 1;
fi
endef
export ENSURE_MASTER_BRANCH_SCRIPT
ENSURE_MASTER_BRANCH := bash -c "$$ENSURE_MASTER_BRANCH_SCRIPT"

help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint: ## check style with flake8
	flake8 {{ cookiecutter.app_name }} tests

test: ## run tests quickly with the default Python
	[ ! -e testserver.log ] || rm testserver.log
	py.test

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source {{ cookiecutter.app_name }} -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/api/{{ cookiecutter.app_name }}*.rst
	sphinx-apidoc -o docs/api {{ cookiecutter.app_name }} {{ cookiecutter.app_name }}/migrations*
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

servedocs: docs ## compile the docs watching for changes
	$(BROWSER) docs/_build/html/index.html
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release-patch:  ## Release a new version: 1.1.1 -> 1.1.2
	$(ENSURE_MASTER_BRANCH)
	git fetch -p --all
	gitchangelog
ifdef EDITOR
	$(EDITOR) CHANGELOG.md
endif
	bumpversion patch --allow-dirty
	git push
	git push --tags

release-minor:  ## Release a new version: 1.1.1 -> 1.2.0
	$(ENSURE_MASTER_BRANCH)
	git fetch -p --all
	gitchangelog
ifdef EDITOR
	$(EDITOR) CHANGELOG.md
endif
	bumpversion minor --allow-dirty
	git push
	git push --tags

release-major:  ## Release a new version: 1.1.1 -> 2.0.0
	$(ENSURE_MASTER_BRANCH)
	git fetch -p --all
	gitchangelog
ifdef EDITOR
	$(EDITOR) CHANGELOG.md
endif
	bumpversion major --allow-dirty
	git push
	git push --tags
