from typing import List

from fastapi import APIRouter, Depends, Response, status

from movieCatalog.models.genres import Genre, GenreCreate
from movieCatalog.services.genres import GenreService

router = APIRouter(
    prefix="/genres",
    tags=['Genres']
)


@router.post('/', response_model=Genre)
def create_genre(
        genre_data: GenreCreate,
        service: GenreService = Depends()
):
    return service.create(genre_data=genre_data)


@router.get('/', response_model=List[Genre])
def get_genres(service: GenreService = Depends()):
    return service.get_genres()


@router.get('/{genre_id}', response_model=Genre)
def gen_genre(
        genre_id: int,
        service: GenreService = Depends()
):
    return service.get_genre(genre_id=genre_id)


@router.delete('/{genre_id}')
def delete_genre(
        genre_id: int,
        service: GenreService = Depends()
):
    service.delete_genre(genre_id=genre_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
