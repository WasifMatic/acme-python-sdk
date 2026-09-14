from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApiResponse(SdkBaseModel):
    code: Optional[int] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    message: Optional[str] = UNSET


class ApiResponseDict(TypedDict):
    code: NotRequired[int]
    type_: NotRequired[str]
    message: NotRequired[str]
