from fastapi import APIRouter

from .genres import router as genres_router

router = APIRouter()
router.include_router(genres_router)
