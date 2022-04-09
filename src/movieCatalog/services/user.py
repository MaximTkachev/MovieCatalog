from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from movieCatalog.database import get_session
from movieCatalog import tables
from movieCatalog.tables import User as UserTable


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
