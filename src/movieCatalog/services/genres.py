from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .. import tables
from movieCatalog.database import get_session
from ..models.genres import GenreCreate, GenreEdit


class GenreService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, genre_data: GenreCreate) -> tables.Genre:
        genre_check = (
            self.session
                .query(tables.Genre)
                .filter_by(name=genre_data.name)
                .first()
        )
        if genre_check:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Genre with the same name already exists")

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

    def edit_genre(self, genre_id: int, genre_data: GenreEdit):
        genre_check = (
            self.session
                .query(tables.Genre)
                .filter(tables.Genre.id != genre_id, tables.Genre.name == genre_data.name)
                .all()
        )

        if genre_check:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Genre with the same name already exists")

        genre = self.get_genre(genre_id=genre_id)
        for field, value in genre_data:
            if value is not None:
                setattr(genre, field, value)

        self.session.commit()
        return genre
