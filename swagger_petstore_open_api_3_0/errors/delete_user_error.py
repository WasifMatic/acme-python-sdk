from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteUserErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteUserError:
    def map(self, response: HttpResponse) -> DeleteUserErrorBody:
        match response.status_code:
            case 400 | 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_user_error_mapper: Final[ErrorMapper[DeleteUserErrorBody]] = _DeleteUserError()
