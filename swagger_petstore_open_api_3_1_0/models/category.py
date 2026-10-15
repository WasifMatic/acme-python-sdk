from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Category(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET


class CategoryDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
