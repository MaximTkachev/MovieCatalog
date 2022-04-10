from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from movieCatalog import tables
from movieCatalog.database import get_session
from movieCatalog.tables import Movie, User


class FavoriteMoviesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_favorite_movies(self, user: User) -> List[tables.Movie]:
        return user.favorite_movies

    def add_movie_to_favorites(self, movie: Movie, user: User):
        user.favorite_movies.append(movie)
        self.session.commit()

    def remove_movie_from_favorites(self, movie: Movie, user: User):
        user.favorite_movies.remove(movie)
        self.session.commit()
