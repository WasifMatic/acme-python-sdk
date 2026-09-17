from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class User(SdkBaseModel):
    id: Optional[int] = UNSET
    username: Optional[str] = UNSET
    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    email: Optional[str] = UNSET
    password: Optional[str] = UNSET
    phone: Optional[str] = UNSET
    user_status: Optional[int] = Field(default=UNSET, alias="userStatus")
    """User Status"""


class UserDict(TypedDict):
    id: NotRequired[int]
    username: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    password: NotRequired[str]
    phone: NotRequired[str]
    user_status: NotRequired[int]
