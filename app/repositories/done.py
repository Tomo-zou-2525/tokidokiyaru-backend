from app.models.done import Done
from app.repositories.base import CRUDBase
from app.schemas.done import (
    DoneCreate,
    DoneUpdate,
)


class CRUDDone(
    CRUDBase[
        Done,
        DoneCreate,
        DoneUpdate,
    ]
):
    pass


done = CRUDDone(model=Done)
