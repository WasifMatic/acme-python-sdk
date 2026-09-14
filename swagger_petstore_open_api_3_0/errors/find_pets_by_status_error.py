from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

FindPetsByStatusErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _FindPetsByStatusError:
    def map(self, response: HttpResponse) -> FindPetsByStatusErrorBody:
        match response.status_code:
            case 400:
                return RawError(response)
            case _:
                return RawError(response)


find_pets_by_status_error_mapper: Final[ErrorMapper[FindPetsByStatusErrorBody]] = _FindPetsByStatusError()
