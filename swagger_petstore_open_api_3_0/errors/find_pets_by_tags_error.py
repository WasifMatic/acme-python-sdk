from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

FindPetsByTagsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _FindPetsByTagsError:
    def map(self, response: HttpResponse) -> FindPetsByTagsErrorBody:
        match response.status_code:
            case 400:
                return RawError(response)
            case _:
                return RawError(response)


find_pets_by_tags_error_mapper: Final[ErrorMapper[FindPetsByTagsErrorBody]] = _FindPetsByTagsError()
