from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeletePetErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeletePetError:
    def map(self, response: HttpResponse) -> DeletePetErrorBody:
        match response.status_code:
            case 400:
                return RawError(response)
            case _:
                return RawError(response)


delete_pet_error_mapper: Final[ErrorMapper[DeletePetErrorBody]] = _DeletePetError()
