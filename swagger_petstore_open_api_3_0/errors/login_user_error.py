from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

LoginUserErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _LoginUserError:
    def map(self, response: HttpResponse) -> LoginUserErrorBody:
        match response.status_code:
            case 400:
                return RawError(response)
            case _:
                return RawError(response)


login_user_error_mapper: Final[ErrorMapper[LoginUserErrorBody]] = _LoginUserError()
