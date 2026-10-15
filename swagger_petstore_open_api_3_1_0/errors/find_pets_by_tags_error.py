from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

FindPetsByTagsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _FindPetsByTagsError:
    def map(self, status_code: int, content: bytes) -> FindPetsByTagsErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


find_pets_by_tags_error_mapper: Final[ErrorMapper[FindPetsByTagsErrorBody]] = _FindPetsByTagsError()
