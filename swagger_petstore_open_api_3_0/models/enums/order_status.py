from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderStatus(str, Enum):
    """Order Status"""

    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"

    __str__ = str.__str__


OrderStatusOrStr: TypeAlias = Annotated[OrderStatus | str, open_enum_validator(OrderStatus)]
