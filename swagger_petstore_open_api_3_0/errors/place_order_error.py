from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

PlaceOrderErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _PlaceOrderError:
    def map(self, response: HttpResponse) -> PlaceOrderErrorBody:
        match response.status_code:
            case 400 | 422:
                return RawError(response)
            case _:
                return RawError(response)


place_order_error_mapper: Final[ErrorMapper[PlaceOrderErrorBody]] = _PlaceOrderError()
