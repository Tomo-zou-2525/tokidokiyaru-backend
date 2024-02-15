from app.models.user import User
from app.repositories.base import CRUDBase
from app.schemas.user import (
    UserCreate,
    UserUpdate,
)


class CRUDUser(
    CRUDBase[
        User,
        UserCreate,
        UserUpdate,
    ]
):
    pass


user = CRUDUser(model=User)
