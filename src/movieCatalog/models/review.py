from pydantic import BaseModel

from movieCatalog.models.auth import User
from movieCatalog.models.movies import Movie


class ReviewBase(BaseModel):
    reviewText: str
    rating: int


class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True


class CreateReview(ReviewBase):
    pass
