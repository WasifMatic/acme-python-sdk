from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

AddPetErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _AddPetError:
    def map(self, status_code: int, content: bytes) -> AddPetErrorBody:
        match status_code:
            case 400 | 422:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


add_pet_error_mapper: Final[ErrorMapper[AddPetErrorBody]] = _AddPetError()
