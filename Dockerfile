FROM python:3.11.5-alpine3.18

ENV LANG=C.UTF-8

WORKDIR /app

RUN : \
    && python3 -m pip install --no-cache-dir --break-system-packages --upgrade pip \
    && python3 -m pip install --no-cache-dir --break-system-packages  \
        fastapi \
        fastapi-sqlalchemy \
        pydantic \
        pydantic[email] \
        alembic \
        psycopg2-binary \
        uvicorn[standard] \
        python-dotenv \
        "importlib-metadata; python_version<\"3.8\"" \
    && :

COPY ./setup.py .
COPY ./pyproject.toml .
COPY ./users_api ./users_api

CMD ["python", "-m", "users_api"]
