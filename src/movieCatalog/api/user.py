from fastapi import APIRouter, Depends

from movieCatalog.models.auth import User, UserData, UserEdit
from movieCatalog.services.auth import get_current_user
from movieCatalog.services.user import UserService

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.get('/', response_model=UserData)
def get_profile_of_specific_user(
        user: User = Depends(get_current_user)
):
    return user


@router.put('/', response_model=UserData)
def edit_profile_of_specific_user(
        user_data: UserEdit,
        user: User = Depends(get_current_user),
        service: UserService = Depends()
):
    return service.edit_user(user_id=user.id, user_data=user_data)
