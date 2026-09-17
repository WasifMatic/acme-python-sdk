from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetOrderByIdErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetOrderByIdError:
    def map(self, response: HttpResponse) -> GetOrderByIdErrorBody:
        match response.status_code:
            case 400 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_order_by_id_error_mapper: Final[ErrorMapper[GetOrderByIdErrorBody]] = _GetOrderByIdError()
