from typing import List

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


@router.get('/', response_model=List[Movie])
def get_list_of_movies(
        service: MovieService = Depends()
):
    return service.get_movies()


@router.get('/{movie_id}', response_model=Movie)
def get_movie_by_id(
        movie_id: int,
        service: MovieService = Depends()
):
    return service.get_movie(movie_id=movie_id)
