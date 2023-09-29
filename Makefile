.PHOHY: default all setup build upgrade-buildsystem \
		install install-dev \
		install-hooks install-dev-requirements \
		test lint fmt format run-hooks \
		clean

PYTHON := python3

SOURCES :=
SOURCES += $(wildcard ./users_api/*.py)
SOURCES += $(wildcard ./users_api/**/*.py)
SOURCES += $(wildcard ./tests/*.py)

DEV_REQUIREMENTS := ./dev-requirements.txt

default: all

all: build

setup:
	$(MAKE) upgrade-buildsystem
	$(MAKE) install-dev-requirements
	$(MAKE) install-hooks
	$(MAKE) install

build:
	$(PYTHON) -m build

upgrade-buildsystem:
	$(PYTHON) -m pip install                \
		--upgrade pip
	$(PYTHON) -m pip install                \
		--upgrade setuptools                \
		--upgrade setuptools-git-versioning \
		--upgrade wheel                     \
		--upgrade build

install:
	$(PYTHON) -m pip install .

uninstall:
	$(PYTHON) -m pip uninstall users-api --yes

install-dev:
	$(PYTHON) -m pip install --editable .

install-hooks:
	pre-commit install

install-dev-requirements:
	@ if [ -z "$(VIRTUAL_ENV)" ]; then               \
		echo "error: running outside of virtualenv"; \
		exit 1;                                      \
	fi

	$(PYTHON) -m pip install -r $(DEV_REQUIREMENTS)

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m black --check $(SOURCES) || true
	$(PYTHON) -m flake8 $(SOURCES) || true
	$(PYTHON) -m mypy $(SOURCES) || true

fmt format:
	$(PYTHON) -m black $(SOURCES)

run-hooks:
	pre-commit run --all-files

clean:
	rm -rf dist/
	rm -rf *.egg-info
