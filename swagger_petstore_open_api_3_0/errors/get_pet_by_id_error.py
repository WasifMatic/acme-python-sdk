from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetPetByIdErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetPetByIdError:
    def map(self, response: HttpResponse) -> GetPetByIdErrorBody:
        match response.status_code:
            case 400 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_pet_by_id_error_mapper: Final[ErrorMapper[GetPetByIdErrorBody]] = _GetPetByIdError()
