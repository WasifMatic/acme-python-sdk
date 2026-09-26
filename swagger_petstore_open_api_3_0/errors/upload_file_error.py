from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

UploadFileErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UploadFileError:
    def map(self, status_code: int, content: bytes) -> UploadFileErrorBody:
        match status_code:
            case 400 | 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


upload_file_error_mapper: Final[ErrorMapper[UploadFileErrorBody]] = _UploadFileError()
