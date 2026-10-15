from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

UpdatePetWithFormErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UpdatePetWithFormError:
    def map(self, status_code: int, content: bytes) -> UpdatePetWithFormErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


update_pet_with_form_error_mapper: Final[ErrorMapper[UpdatePetWithFormErrorBody]] = _UpdatePetWithFormError()
