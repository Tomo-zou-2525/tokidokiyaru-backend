from typing import Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(
    Generic[
        ModelType,
        CreateSchemaType,
        UpdateSchemaType,
    ]
):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int | str) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_list(self, db: Session) -> list[ModelType]:
        query = db.query(self.model)

        return query.all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        # by_alias=Falseにしないとalias側(CamelCase)が採用されてしまう
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()

        return db_obj

    def update(
        self, id: int, db: Session, obj_in: UpdateSchemaType
    ) -> ModelType | None:
        target: ModelType | None = (
            db.query(self.model).filter(self.model.id == id).first()
        )
        target_dict = jsonable_encoder(target, by_alias=False)
        update_dict = obj_in.model_dump(exclude_unset=True)
        for field in target_dict:
            if field in update_dict:
                setattr(target, field, update_dict[field])

        db.add(target)
        db.commit()
        return target

    def hard_delete(self, db: Session, id: int) -> ModelType | None:
        target: ModelType | None = (
            db.query(self.model).filter(self.model.id == id).first()
        )
        if target is None:
            return None
        db.delete(target)
        db.commit()
        return target
