from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.order_status import OrderStatusOrStr


class Order(SdkBaseModel):
    id: Optional[int] = UNSET
    pet_id: Optional[int] = Field(default=UNSET, alias="petId")
    quantity: Optional[int] = UNSET
    ship_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="shipDate")
    status: Optional[OrderStatusOrStr] = UNSET
    """Order Status"""

    complete: Optional[bool] = UNSET


class OrderDict(TypedDict):
    id: NotRequired[int]
    pet_id: NotRequired[int]
    quantity: NotRequired[int]
    ship_date: NotRequired[RFC3339DateTime]
    status: NotRequired[OrderStatusOrStr]
    complete: NotRequired[bool]
