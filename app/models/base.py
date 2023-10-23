from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column


class ModelBase:
    id = mapped_column(Integer, primary_key=True, sort_order=-10)
    order_num = mapped_column(
        Integer, nullable=False, server_default="0", sort_order=97
    )
