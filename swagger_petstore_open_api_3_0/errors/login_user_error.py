from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

LoginUserErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LoginUserError:
    def map(self, status_code: int, content: bytes) -> LoginUserErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


login_user_error_mapper: Final[ErrorMapper[LoginUserErrorBody]] = _LoginUserError()
