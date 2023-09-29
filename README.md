# Users API

API written in FastAPI

> Note: Project was tested only with Podman (instead of Docker)

## Run

* Docker compose

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

## Development
