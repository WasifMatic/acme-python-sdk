from __future__ import annotations

from typing import Generic

from .core import RawClientT
from .server.server import Server
from .server.server_config import ServerConfig, ServerConfigOrDict

DEFAULT_TIMEOUT = 30.0


class BaseSwaggerPetstoreOpenApi30Client(Generic[RawClientT]):
    _raw_client: RawClientT

    def __init__(self, *, server_config: ServerConfigOrDict | None = None, timeout: float = DEFAULT_TIMEOUT) -> None:
        if not timeout > 0:
            raise ValueError(f"timeout must be greater than 0; got {timeout!r}")
        self._server = Server(ServerConfig.coerce(server_config))
