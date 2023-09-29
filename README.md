# Users API

API written in FastAPI

> Note: Project was tested only with Podman (instead of Docker)

## Run

* Docker compose

```shell
docker compose up
```

* Docker image

```shell
docker run -it --expose 8000:8000 --mount=bind,src=./.env,dst=/app/.env <image-name>
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
