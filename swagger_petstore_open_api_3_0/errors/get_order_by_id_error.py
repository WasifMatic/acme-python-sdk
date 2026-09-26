from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetOrderByIdErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetOrderByIdError:
    def map(self, status_code: int, content: bytes) -> GetOrderByIdErrorBody:
        match status_code:
            case 400 | 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_order_by_id_error_mapper: Final[ErrorMapper[GetOrderByIdErrorBody]] = _GetOrderByIdError()
