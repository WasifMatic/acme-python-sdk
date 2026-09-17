from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TagModel(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET


class TagModelDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
