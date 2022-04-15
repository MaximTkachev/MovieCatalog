from typing import List

from fastapi import Depends, HTTPException, status

from movieCatalog import tables
from movieCatalog.database import Session, get_session
from movieCatalog.models.review import CreateReview, ReviewUpdate
from movieCatalog.tables import Review


class ReviewService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_review(self, review_data: CreateReview,
                      user_id: int, movie_id: int):
        if review_data.rating < 0 or review_data.rating > 10:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Incorrect rating value")
        
        review = tables.Review(
            reviewText=review_data.reviewText,
            rating=review_data.rating,
            authorId=user_id,
            movieId=movie_id
        )
        self.session.add(review)
        self.session.commit()

    def get_review(self, review_id: int) -> Review:
        review = (
            self.session
                .query(tables.Review)
                .filter_by(id=review_id)
                .first()
        )

        if not review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return review

    def delete_review(self, review_id):
        movie = self.get_review(review_id=review_id)
        self.session.delete(movie)
        self.session.commit()

    def get_list_of_reviews(self) -> List[Review]:
        reviews = (
            self.session
            .query(tables.Review)
            .all()
        )

        return reviews

    def edit_review(self, review_id: int, author_id: int, review_data: ReviewUpdate) -> Review:
        review = self.get_review(review_id=review_id)
        if review.authorId != author_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        for field, value in review_data:
            if value is not None:
                setattr(review, field, value)
        self.session.commit()
        return review
