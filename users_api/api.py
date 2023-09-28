from __future__ import annotations

import fastapi

api_router = fastapi.APIRouter(prefix="/api/v1/users")


@api_router.get("")
async def users_index():
    return {"Hello": "World"}
