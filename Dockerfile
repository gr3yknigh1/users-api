FROM python:3.11.5-alpine3.18

ENV LANG=C.UTF-8

WORKDIR /app

COPY ./setup.py .
COPY ./pyproject.toml .

COPY ./users_api ./users_api

RUN : \
    && python3 -m pip install --no-cache-dir --break-system-packages . \
    && :

CMD ["python", "-m", "users_api"]
