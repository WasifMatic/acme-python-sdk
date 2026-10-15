from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PetStatus(str, Enum):
    """pet status in the store"""

    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

    __str__ = str.__str__


PetStatusOrStr: TypeAlias = Annotated[PetStatus | str, open_enum_validator(PetStatus)]
