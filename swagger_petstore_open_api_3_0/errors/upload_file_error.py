from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

UploadFileErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UploadFileError:
    def map(self, response: HttpResponse) -> UploadFileErrorBody:
        match response.status_code:
            case 400 | 404:
                return RawError(response)
            case _:
                return RawError(response)


upload_file_error_mapper: Final[ErrorMapper[UploadFileErrorBody]] = _UploadFileError()
