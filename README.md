# Users API

Some users API written in FastAPI

> Note: Project was tested only with Podman (instead of Docker)

## Stack

* FastAPI (uvicorn)
* PostgresSQL
* SQLAlchemy

## Usage

Checkout docs at `<USERS_API_HOST>:<USERS_API_PORT>/docs` for API details

## Configuration

Sample `.env` file (`./examples/dotenv`)

```env

# Sample Dotenv file

USERS_API_HOST=0.0.0.0
USERS_API_PORT=8000
USERS_API_LOG_LEVEL=DEBUG

POSTGRES_USER=users_api
POSTGRES_PASSWORD=pass
POSTGRES_ADDR=172.17.0.1
POSTGRES_PORT=5432
POSTGRES_DB=users

```

## Run

You need to setup environment variables in order to start server. You can use `examples/dotenv` for that.

> Note: You can copy `./examples/dotenv` to `./.env` for testing

```shell
docker compose up
```

## Build

* Docker image

```shell
docker build . --tag <image-name>
```

* Python wheel

(See `dist/` directory)

```shell
make upgrade-buildsystem build
```

Or just

```shell
python3 -m pip install \
    --upgrade pip
python3 -m pip install \
    --upgrade setuptools \
    --upgrade setuptools-git-versioning \
    --upgrade wheel \
    --upgrade build
python3 -m build
```

## Development setup

* Automatic

```shell
make setup
```

* Manual (make sure use to `virtualenv`)

```shell
python3 -m pip install -r dev-requirements.txt
pre-commit install
python3 -m pip install -e .
```
