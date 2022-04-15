from typing import Optional

from pydantic import BaseModel


class ReviewBase(BaseModel):
    reviewText: str
    rating: int


class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True


class CreateReview(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    reviewText: Optional[str]
    rating: Optional[int]
