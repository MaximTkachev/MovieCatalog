from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from movieCatalog.database import get_session
from ..models.movies import MovieCreate
from .. import tables


class MovieService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_movie(self, movie_data: MovieCreate) -> tables.Movie:
        list_of_genres = (
            self.session
            .query(tables.Genre)
            .filter(tables.Genre.id.in_(movie_data.genres))
            .all()
        )

        movie = tables.Movie(
            name=movie_data.name,
            year=movie_data.year,
            country=movie_data.country,
            budget=movie_data.budget,
            fees=movie_data.fees,
            genres=list_of_genres
        )
        self.session.add(movie)
        self.session.commit()

        return movie
