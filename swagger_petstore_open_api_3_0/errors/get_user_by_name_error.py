from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetUserByNameErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetUserByNameError:
    def map(self, response: HttpResponse) -> GetUserByNameErrorBody:
        match response.status_code:
            case 400 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_user_by_name_error_mapper: Final[ErrorMapper[GetUserByNameErrorBody]] = _GetUserByNameError()
