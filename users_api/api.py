from __future__ import annotations

import fastapi

api_router = fastapi.APIRouter(prefix="/api/v1")


@api_router.get("/users")
async def get_users_list():
    return {"Hello": "World"}


@api_router.get("/health")
async def check_server_health():
    return "OK"
