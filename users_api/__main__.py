from __future__ import annotations

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("package-name").version
except DistributionNotFound:
    __version__ = "0.0.1"

import logging
import logging.config

import uvicorn
import fastapi

from .api import api_router
from .config import read_env


app = fastapi.FastAPI(
    title="Users API",
    summary=None,
    description="Some users API written in FastAPI",
    version=__version__,
)
app.include_router(api_router)


def main() -> int:
    config = read_env()

    # TODO(gr3yknigh1): Use structlog and reformat unviron log format
    logging.basicConfig(
        level=config.get("USERS_API_LOG_LEVEL", "INFO"),
        format="(%(threadName)s) :: %(name)s :: [%(levelname)s]: %(message)s",
    )
    logger = logging.getLogger("users_api")
    logger.info(f"Starting API v{__version__}")

    uvicorn.run(
        app=app,
        host=config["USERS_API_HOST"],
        port=int(config["USERS_API_PORT"]),
        reload=False,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
