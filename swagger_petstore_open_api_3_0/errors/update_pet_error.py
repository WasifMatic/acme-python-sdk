from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

UpdatePetErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UpdatePetError:
    def map(self, response: HttpResponse) -> UpdatePetErrorBody:
        match response.status_code:
            case 400 | 404 | 422:
                return RawError(response)
            case _:
                return RawError(response)


update_pet_error_mapper: Final[ErrorMapper[UpdatePetErrorBody]] = _UpdatePetError()
