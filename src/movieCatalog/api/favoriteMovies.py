from typing import List

from fastapi import APIRouter, Depends, Response, status

from movieCatalog.models.auth import User
from movieCatalog.models.movies import Movie
from movieCatalog.services.auth import get_current_user
from movieCatalog.services.favoriteMovies import FavoriteMoviesService
from movieCatalog.services.movies import MovieService
from movieCatalog.services.user import UserService

router = APIRouter(
    prefix="/favorites",
    tags=['Favorite movies']
)


@router.get('/', response_model=List[Movie])
def get_favorite_movies_for_current_user(
        user: User = Depends(get_current_user),
        service: FavoriteMoviesService = Depends(),
        user_service: UserService = Depends()
):
    return service.get_favorite_movies(
        user=user_service.get_user_as_table(user_id=user.id)
    )


@router.post('/{movie_id}')
def add_movie_to_favorites(
        movie_id: int,
        user: User = Depends(get_current_user),
        favorite_movies_service: FavoriteMoviesService = Depends(),
        movies_service: MovieService = Depends(),
        user_service: UserService = Depends()
):
    favorite_movies_service.add_movie_to_favorites(
        movie=movies_service.get_movie(movie_id=movie_id),
        user=user_service.get_user_as_table(user_id=user.id)
    )
    return Response(status_code=status.HTTP_200_OK)


@router.delete('/{movie_id}')
def remove_movie_from_favorites(
        movie_id: int,
        user: User = Depends(get_current_user),
        favorite_movies_service: FavoriteMoviesService = Depends(),
        movies_service: MovieService = Depends(),
        user_service: UserService = Depends()
):
    favorite_movies_service.remove_movie_from_favorites(
        movie=movies_service.get_movie(movie_id=movie_id),
        user=user_service.get_user_as_table(user_id=user.id)
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
