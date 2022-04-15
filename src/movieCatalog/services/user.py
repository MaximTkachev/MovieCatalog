from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from movieCatalog.database import get_session
from movieCatalog import tables
from movieCatalog.models.auth import UserEdit, UserData
from movieCatalog.tables import User as UserTable
from .auth import hash_password


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_user_as_table(self, user_id: int) -> UserTable:
        user = (
            self.session
            .query(tables.User)
            .filter_by(id=user_id)
            .first()
        )
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return user

    def edit_user(self, user_id: int, user_data: UserEdit) -> UserData:
        user = self.get_user_as_table(user_id=user_id)
        for field, value in user_data:
            if value is not None:
                if field == "password":
                    value = hash_password(value)
                    setattr(user, "password_hash", value)
                setattr(user, field, value)

        self.session.commit()
        return user
