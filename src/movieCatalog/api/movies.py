from fastapi import APIRouter, Depends

from ..models.movies import MovieCreate, Movie
from ..services.movies import MovieService

router = APIRouter(
    prefix="/movies"
)


@router.post('/', response_model=Movie)
def create_movie(
        movie_data: MovieCreate,
        service: MovieService = Depends()
):
    return service.create_movie(movie_data=movie_data)
