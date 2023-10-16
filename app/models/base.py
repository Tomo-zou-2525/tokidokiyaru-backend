from sqlalchemy import DATETIME, Integer, func
from sqlalchemy.orm import mapped_column


class ModelBase:
    id = mapped_column(Integer, primary_key=True, sort_order=-10)
    order_num = mapped_column(
        Integer, nullable=False, server_default="0", sort_order=97
    )
    created_at = mapped_column(
        DATETIME, nullable=False, server_default=func.now(), sort_order=98
    )
    updated_at = mapped_column(
        DATETIME,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        sort_order=99,
    )
