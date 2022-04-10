from typing import List

from fastapi import APIRouter, Depends, Response, status

from ..models.auth import User
from ..models.review import CreateReview, Review
from ..services.auth import get_current_user
from ..services.review import ReviewService

router = APIRouter(
    prefix='/review',
    tags=['Review']
)


@router.get('/', response_model=List[Review])
def get_list_of_reviews(
    service: ReviewService = Depends()
):
    return service.get_list_of_reviews()


@router.get('/{review_id}', response_model=Review)
def get_review_by_id(
        review_id: int,
        service: ReviewService = Depends()
):
    return service.get_review(review_id=review_id)


@router.post('/')
def add_review_to_film(
        movie_id: int,
        review_data: CreateReview,
        user: User = Depends(get_current_user),
        service: ReviewService = Depends()
):
    service.create_review(
        review_data=review_data,
        user_id=user.id,
        movie_id=movie_id
    )
    return Response(status_code=status.HTTP_200_OK)


@router.delete('/{review_id}')
def remove_review_to_film(
        review_id: int,
        service: ReviewService = Depends()
):
    service.delete_review(review_id=review_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
