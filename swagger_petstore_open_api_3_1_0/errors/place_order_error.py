from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

PlaceOrderErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _PlaceOrderError:
    def map(self, status_code: int, content: bytes) -> PlaceOrderErrorBody:
        match status_code:
            case 400 | 422:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


place_order_error_mapper: Final[ErrorMapper[PlaceOrderErrorBody]] = _PlaceOrderError()
