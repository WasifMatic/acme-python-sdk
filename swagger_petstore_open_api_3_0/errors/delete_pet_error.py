from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeletePetErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeletePetError:
    def map(self, status_code: int, content: bytes) -> DeletePetErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_pet_error_mapper: Final[ErrorMapper[DeletePetErrorBody]] = _DeletePetError()
