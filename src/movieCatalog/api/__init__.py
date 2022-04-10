from fastapi import APIRouter

from .genres import router as genres_router
from .movies import router as movies_router
from .auth import router as auth_router
from .favoriteMovies import router as favorite_movies_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(genres_router)
router.include_router(movies_router)
router.include_router(favorite_movies_router)
