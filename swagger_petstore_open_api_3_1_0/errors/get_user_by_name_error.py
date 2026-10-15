from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetUserByNameErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetUserByNameError:
    def map(self, status_code: int, content: bytes) -> GetUserByNameErrorBody:
        match status_code:
            case 400 | 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_user_by_name_error_mapper: Final[ErrorMapper[GetUserByNameErrorBody]] = _GetUserByNameError()
