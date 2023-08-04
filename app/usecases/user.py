from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.get("/users", response_model=List[UserResponse])
def read_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    users = repository.get_users(skip=skip, limit=limit)
    return users


@router.post("/users", response_model=UserResponse)
def create_user(
        user: UserCreate, db: Session = Depends(get_db)):
    repository = UserRepository(db)

    return repository.create_user(user=user)
