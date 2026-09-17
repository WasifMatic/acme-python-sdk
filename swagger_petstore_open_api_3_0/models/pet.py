from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .category import Category, CategoryDict
from .enums.pet_status import PetStatusOrStr
from .tag_model import TagModel, TagModelDict


class Pet(SdkBaseModel):
    id: Optional[int] = UNSET
    name: str
    category: Optional[Category] = UNSET
    photo_urls: list[str] = Field(alias="photoUrls")
    tags: Optional[list[TagModel]] = UNSET
    status: Optional[PetStatusOrStr] = UNSET
    """pet status in the store"""


class PetDict(TypedDict):
    id: NotRequired[int]
    name: str
    category: NotRequired[CategoryDict]
    photo_urls: list[str]
    tags: NotRequired[list[TagModelDict]]
    status: NotRequired[PetStatusOrStr]
