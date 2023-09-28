# Users API

API written in FastAPI

## Run

* Docker image

```shell
docker run -it -p 8000:8000 --mount=bind,src=./.env,dst=/app/.env <image-name>
```

## Build

* Docker image

```shell
docker build .
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
