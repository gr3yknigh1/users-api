from __future__ import annotations
from typing import MutableMapping, Mapping, Any

import os

from dotenv import load_dotenv

load_dotenv(".env")

REQURED_ENV_KEYS = ("USERS_API_HOST", "USERS_API_PORT")


def read_env() -> Mapping[str, Any]:
    # TODO(gr3yknigh1): Move to config validation to sep function
    config: MutableMapping[str, Any] = os.environ

    for required_env_key in REQURED_ENV_KEYS:
        if required_env_key not in config.keys():
            raise ValueError(
                f"Required env value isn't set: {required_env_key!r}"
            )

    return config
