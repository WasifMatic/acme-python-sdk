from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

FindPetsByStatusErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _FindPetsByStatusError:
    def map(self, status_code: int, content: bytes) -> FindPetsByStatusErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


find_pets_by_status_error_mapper: Final[ErrorMapper[FindPetsByStatusErrorBody]] = _FindPetsByStatusError()
