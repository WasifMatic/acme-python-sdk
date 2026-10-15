from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteOrderErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteOrderError:
    def map(self, status_code: int, content: bytes) -> DeleteOrderErrorBody:
        match status_code:
            case 400 | 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_order_error_mapper: Final[ErrorMapper[DeleteOrderErrorBody]] = _DeleteOrderError()
