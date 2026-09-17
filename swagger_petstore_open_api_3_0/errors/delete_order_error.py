from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteOrderErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteOrderError:
    def map(self, response: HttpResponse) -> DeleteOrderErrorBody:
        match response.status_code:
            case 400 | 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_order_error_mapper: Final[ErrorMapper[DeleteOrderErrorBody]] = _DeleteOrderError()
