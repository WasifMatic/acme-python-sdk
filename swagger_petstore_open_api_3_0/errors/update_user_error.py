from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

UpdateUserErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UpdateUserError:
    def map(self, response: HttpResponse) -> UpdateUserErrorBody:
        match response.status_code:
            case 400 | 404:
                return RawError(response)
            case _:
                return RawError(response)


update_user_error_mapper: Final[ErrorMapper[UpdateUserErrorBody]] = _UpdateUserError()
