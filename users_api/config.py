from __future__ import annotations
from typing import MutableMapping, Mapping, Any, Optional

import os

from dotenv import load_dotenv

load_dotenv(".env")

REQURED_ENV_KEYS = ("USERS_API_HOST", "USERS_API_PORT")

_config: Optional[Mapping[str, Any]] = None


def read_env() -> Mapping[str, Any]:
    global _config

    if _config is not None:
        return _config

    # TODO(gr3yknigh1): Move to config validation to sep function
    config: MutableMapping[str, Any] = os.environ

    for required_env_key in REQURED_ENV_KEYS:
        if required_env_key not in config.keys():
            raise ValueError(
                f"Required env value isn't set: {required_env_key!r}"
            )

    return config


__all__ = ("read_env",)
