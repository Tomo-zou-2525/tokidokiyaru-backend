from app.models.run_date import RunDate
from app.repositories.base import CRUDBase
from app.schemas.run_date import (
    RunDateCreate,
    RunDateUpdate,
)


class CRUDRunDate(
    CRUDBase[
        RunDate,
        RunDateCreate,
        RunDateUpdate,
    ]
):
    pass


run_date = CRUDRunDate(model=RunDate)
