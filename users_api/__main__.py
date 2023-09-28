from __future__ import annotations
from typing import MutableMapping, Mapping, Any, Callable

import logging
import logging.config
import copy

from dotenv import dotenv_values
import uvicorn
import fastapi

from .api import api_router

REQURED_ENV_KEYS = ("USERS_API_HOST", "USERS_API_PORT")
MAP_ENV_KEYS: Mapping[str, Callable[[Any], Any]] = {"USERS_API_PORT": int}

app = fastapi.FastAPI()
app.include_router(api_router)


def main() -> int:
    # TODO(gr3yknigh1): Move to config validation to sep function
    config: MutableMapping[str, Any] = dotenv_values(".env")

    for required_env_key in REQURED_ENV_KEYS:
        if required_env_key not in config.keys():
            raise ValueError(
                f"Required env value isn't set: {required_env_key!r}"
            )

    for key, value in copy.copy(config).items():
        if key not in MAP_ENV_KEYS.keys():
            continue
        config[key] = MAP_ENV_KEYS[key](value)

    # TODO(gr3yknigh1): Use structlog and reformat unviron log format
    logging.basicConfig(
        level=config.get("USERS_API_LOG_LEVEL", "INFO"),
        format="(%(threadName)s) :: %(name)s :: [%(levelname)s]: %(message)s",
    )
    logger = logging.getLogger("users_api")
    logger.debug(f"Config: {config!r}")

    uvicorn.run(
        app=app,
        host=config["USERS_API_HOST"],
        port=config["USERS_API_PORT"],
        reload=False,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
