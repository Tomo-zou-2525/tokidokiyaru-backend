# Import all the models, so that Base has them before being
# imported by Alembic

from app.models.run_date import RunDate  # noqa
from app.models.task import Task  # noqa
from app.models.user import User  # noqa
