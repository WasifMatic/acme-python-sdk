"""The result of one API call, as a value rather than an exception.

``ApiResult`` is a tagged union: a call yields exactly one of :class:`Success` or :class:`Failure`,
never both and never neither, so which one you hold is a fact the type checker can see. Narrow it
with ``match`` or ``isinstance`` and the payload or error comes with it:

    match client.body_params.with_raw_response.send_model(employee):
        case Success(payload=confirmation):
            ...
        case Failure(error=err):
            ...

Both variants are frozen dataclasses, so pattern matching needs nothing added. ``.unwrap()`` is the
shortcut for callers that would rather not branch -- it returns the payload or raises.

Each carries the response's **head** -- its status and headers -- as fields of its own rather than a
response object. There is no body beside them: the body *is* the payload on a success, and on a
failure it is the error, reachable through :class:`RawError` where the operation documents no schema
for it. A no-content operation therefore cannot show a caller the body it discarded; reaching one
deliberately is future work, and an empty ``content`` on a response object was the wrong way to
advertise its absence.

:class:`RawError` lives here too: it is the error type a :class:`Failure` carries when the operation
does not document the status that came back."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Generic, NoReturn, TypeAlias, TypeVar

from ._internal.wire import parse_json
from .exceptions import ApiError

T = TypeVar("T")
E = TypeVar("E")


@dataclass(frozen=True, slots=True)
class Success(Generic[T]):
    """A successful (2xx) API call carrying the decoded ``payload``."""

    payload: T
    status_code: int
    headers: Mapping[str, str] = field(repr=False)
    """Header names lowercased, per the transports' obligation -- look keys up in lowercase.

    Kept out of the generated repr: a response's headers carry ``set-cookie``, so a result printed
    in a log line or a debugger pane would otherwise hand over a session secret. The status stays,
    because identifying the result is the whole job of the string form (ADR-0017)."""

    def unwrap(self) -> T:
        """Collapse this result to its parsed value.

        Returns:
            The decoded payload. This variant never raises."""
        return self.payload


@dataclass(frozen=True, slots=True)
class Failure(Generic[E]):
    """A failed (non-2xx) API call carrying the decoded error body ``error``.

    ``error`` is the typed error payload directly (a union of the operation's
    documented schemas, or :class:`RawError` for an unmapped status) -- not a wrapper."""

    error: E
    status_code: int
    headers: Mapping[str, str] = field(repr=False)
    """Header names lowercased, per the transports' obligation -- look keys up in lowercase.

    Kept out of the generated repr: a response's headers carry ``set-cookie``, so a result printed
    in a log line or a debugger pane would otherwise hand over a session secret. The status stays,
    because identifying the result is the whole job of the string form (ADR-0017)."""

    def unwrap(self) -> NoReturn:
        """Collapse this result to its parsed value, which for a failure means raising.

        Raises:
            ApiError: Always, carrying this result's ``error`` and the response head."""
        raise ApiError(error=self.error, status_code=self.status_code, headers=self.headers)


# One call yields exactly one of these; narrow with ``match`` or ``isinstance``,
# or collapse to the parsed value with ``.unwrap()``.
ApiResult: TypeAlias = Success[T] | Failure[E]


@dataclass(frozen=True, slots=True)
class RawError:
    """Undecoded fallback body (unmapped status / no declared schema).

    Holds the status and the bytes themselves rather than a response, so the one object that *is*
    the error carries everything it needs to describe itself. Decoded on demand --
    ``RawError(status_code, content)``."""

    status_code: int
    content: bytes

    def text(self, encoding: str = "utf-8") -> str:
        """Decode the undecoded body as text, for a log line or a diagnostic.

        Args:
            encoding: Character encoding to decode with.

        Returns:
            The body as text, undecodable bytes replaced rather than raising."""
        return self.content.decode(encoding, errors="replace")

    def json(self) -> Any:
        """Parse the undecoded body as JSON.

        Returns:
            Whatever the body parses to.

        Raises:
            ValueError: If the body is not valid JSON."""
        return parse_json(self.content)

    def __repr__(self) -> str:
        # Identify by status only -- the (undecoded, possibly large, binary, or sensitive) body is
        # deliberately kept out of the string form. Read it on demand via ``text``/``json``.
        return f"{type(self).__name__}(status_code={self.status_code})"
