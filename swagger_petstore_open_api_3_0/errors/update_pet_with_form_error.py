from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

UpdatePetWithFormErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UpdatePetWithFormError:
    def map(self, response: HttpResponse) -> UpdatePetWithFormErrorBody:
        match response.status_code:
            case 400:
                return RawError(response)
            case _:
                return RawError(response)


update_pet_with_form_error_mapper: Final[ErrorMapper[UpdatePetWithFormErrorBody]] = _UpdatePetWithFormError()
