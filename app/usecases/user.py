from typing import List

from faker import Faker
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.repositories.user import user
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate,
)


router = APIRouter()


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)) -> User:
    user_data = user.get(id=id, db=db)

    return user_data


@router.get("", response_model=List[UserResponse])
def get_user_list(db: Session = Depends(get_db)) -> List[User]:
    user_data = user.get_list(db=db)

    return user_data


@router.post("", response_model=UserResponse)
def create_user(data_in: UserCreate, db: Session = Depends(get_db)) -> User:
    return user.create(db=db, obj_in=data_in)


@router.post("/rand", response_model=UserResponse)
def create_rand_user(db: Session = Depends(get_db)) -> User:
    fake = Faker("ja_JP")
    data_in = UserCreate(
        email=fake.email(),
        name=fake.name(),
        password="test",
    )

    return user.create(db=db, obj_in=data_in)


@router.put("/{id}", response_model=UserResponse)
def update_user(id: int, data_in: UserUpdate, db: Session = Depends(get_db)) -> User:
    return user.update(db=db, id=id, obj_in=data_in)


@router.delete("/{id}", response_model=UserResponse)
def hard_delete_user(id: int, db: Session = Depends(get_db)) -> User:
    return user.hard_delete(db=db, id=id)
