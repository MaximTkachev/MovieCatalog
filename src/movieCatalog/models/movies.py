from typing import Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    year: Optional[str]
    country: Optional[str]
    budget: Optional[int]
    fees: Optional[int]


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    name: Optional[str]
