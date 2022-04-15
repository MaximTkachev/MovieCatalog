from typing import Optional, List

from pydantic import BaseModel

from movieCatalog.models.genres import Genre


class MovieBase(BaseModel):
    name: str
    year: Optional[str]
    country: Optional[str]
    budget: Optional[int]
    fees: Optional[int]


class Movie(MovieBase):
    id: int
    genres: List[Genre] = []

    class Config:
        orm_mode = True


class MovieCreate(MovieBase):
    genres: List[int] = []


class Rating(BaseModel):
    value: float


class MovieEdit(BaseModel):
    name: Optional[str]
