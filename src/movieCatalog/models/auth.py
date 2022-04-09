from typing import List

from pydantic import BaseModel

from movieCatalog.models.movies import Movie


class BaseUser(BaseModel):
    username: str
    email: str
    name: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    favorite_movies: List[Movie] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
