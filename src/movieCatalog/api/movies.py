from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status

from ..models.auth import User
from ..models.movies import MovieCreate, Movie, Rating
from ..services.auth import get_current_user
from ..services.movies import MovieService

router = APIRouter(
    prefix="/movies",
    tags=['Movies']
)


@router.post('/', response_model=Movie)
def create_movie(
        movie_data: MovieCreate,
        user: User = Depends(get_current_user),
        service: MovieService = Depends()
):
    return service.create_movie(movie_data=movie_data)


@router.get('/', response_model=List[Movie])
def get_list_of_movies(
        name: Optional[str] = None,
        service: MovieService = Depends()
):
    return service.get_movies(name_template=name)


@router.get('/{movie_id}', response_model=Movie)
def get_movie_by_id(
        movie_id: int,
        service: MovieService = Depends()
):
    return service.get_movie(movie_id=movie_id)


@router.get('/{movie_id}/rating', response_model=Rating)
def get_rating_of_movie(
        movie_id: int,
        service: MovieService = Depends()
):
    return service.get_rating_of_movie(movie_id=movie_id)


@router.delete('/{movie_id}')
def delete_movie_from_collection(
        movie_id: int,
        user: User = Depends(get_current_user),
        service: MovieService = Depends()
):
    service.delete_movie(movie_id=movie_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
