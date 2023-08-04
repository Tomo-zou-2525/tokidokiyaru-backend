import hashlib

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas import schemas


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: schemas.UserCreate):
        db_user = User(
            name=user.name,
            email=user.email,
            password=hashlib.sha256(user.password.encode()).hexdigest()
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
