from app.entrypoint.api.v1.box_router import router as box_router
from fastapi import APIRouter

router = APIRouter(prefix="/v1")
router.include_router(box_router, prefix="/box")