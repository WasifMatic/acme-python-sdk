"""The SDK's single exception type."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Generic

from typing_extensions import TypeVar

E = TypeVar("E", default=object)


class ApiError(Exception, Generic[E]):
    """A failed API call, raised by the parsed response mode.

    ``error`` is the decoded response body -- a typed union of the operation's documented
    error schemas, or :class:`RawError` for a status the operation does not document. That
    payload *is* the information, so neither string form embeds it: ``str`` and ``repr``
    identify the failure by status and error type only, which keeps response bodies out of logs
    and tracebacks. Read ``.error`` to inspect it."""

    def __init__(self, error: E, status_code: int, headers: Mapping[str, str]) -> None:
        # Composed once: ``Exception.__str__`` returns a single argument verbatim, so
        # ``args[0]`` and ``str(self)`` are the same string by construction.
        super().__init__(f"HTTP {status_code}: {type(error).__name__}")
        self.error: E = error
        self.status_code = status_code
        self.headers: Mapping[str, str] = headers
        """Header names lowercased, per the transports' obligation -- look keys up in lowercase."""

    def __repr__(self) -> str:
        return f"{type(self).__name__}(status_code={self.status_code}, error={type(self.error).__name__})"

    def __reduce__(self) -> tuple[type[ApiError[E]], tuple[E, int, Mapping[str, str]], dict[str, Any]]:
        # ``BaseException``'s default reduce replays ``args`` through ``__init__``, which takes
        # three arguments -- so pickling and copying both fail without this. The state mapping is
        # what carries ``__notes__`` and any subclass attribute across the round trip.
        return (type(self), (self.error, self.status_code, self.headers), self.__dict__)
