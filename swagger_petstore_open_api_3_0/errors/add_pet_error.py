from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

AddPetErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _AddPetError:
    def map(self, response: HttpResponse) -> AddPetErrorBody:
        match response.status_code:
            case 400 | 422:
                return RawError(response)
            case _:
                return RawError(response)


add_pet_error_mapper: Final[ErrorMapper[AddPetErrorBody]] = _AddPetError()
