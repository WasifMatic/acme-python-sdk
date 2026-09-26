from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

UpdateUserErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UpdateUserError:
    def map(self, status_code: int, content: bytes) -> UpdateUserErrorBody:
        match status_code:
            case 400 | 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


update_user_error_mapper: Final[ErrorMapper[UpdateUserErrorBody]] = _UpdateUserError()
