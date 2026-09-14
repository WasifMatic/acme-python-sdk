from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .category import Category, CategoryDict
from .enums.pet_status import PetStatusOrStr
from .tag import Tag, TagDict


class Pet(SdkBaseModel):
    id: Optional[int] = UNSET
    name: str
    category: Optional[Category] = UNSET
    photo_urls: list[str] = Field(alias="photoUrls")
    tags: Optional[list[Tag]] = UNSET
    status: Optional[PetStatusOrStr] = UNSET
    """pet status in the store"""


class PetDict(TypedDict):
    id: NotRequired[int]
    name: str
    category: NotRequired[Category | CategoryDict]
    photo_urls: list[str]
    tags: NotRequired[list[Tag | TagDict]]
    status: NotRequired[PetStatusOrStr]
