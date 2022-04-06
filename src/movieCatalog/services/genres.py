from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .. import tables
from movieCatalog.database import get_session
from ..models.genres import GenreCreate


class GenreService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, genre_data: GenreCreate) -> tables.Genre:
        genre = tables.Genre(
            **genre_data.dict()
        )
        self.session.add(genre)
        self.session.commit()
        return genre

    def get_genres(self) -> List[tables.Genre]:
        genres = (
            self.session
            .query(tables.Genre)
            .all()
        )
        return genres

    def get_genre(self, genre_id: int) -> tables.Genre:
        genre = (
            self.session
            .query(tables.Genre)
            .filter_by(id=genre_id)
            .first()
        )

        if not genre:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return genre

    def delete_genre(self, genre_id: int):
        genre = self.get_genre(genre_id=genre_id)
        self.session.delete(genre)
        self.session.commit()
