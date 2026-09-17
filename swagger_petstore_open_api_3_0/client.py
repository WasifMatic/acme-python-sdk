from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.pet_api import PetApi
from .apis.store import Store
from .apis.user_api import UserApi
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseSwaggerPetstoreOpenApi30Client
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    no_auth,
    param,
)
from .server.server_config import ServerConfigOrDict


class SwaggerPetstoreOpenApi30Client(BaseSwaggerPetstoreOpenApi30Client[RawClient]):
    def __init__(
        self,
        *,
        server_config: ServerConfigOrDict | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        petstore_auth: str | None = None,
        api_key: str | None = None,
    ) -> None:
        super().__init__(server_config=server_config, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "SwaggerPetstoreOpenApi30Client/1.0.26 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.26"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            petstore_auth=ApiKeyHeaderScheme("Authorization", petstore_auth) if petstore_auth is not None else no_auth,
            api_key=ApiKeyHeaderScheme("api_key", api_key) if api_key is not None else no_auth,
        )

    @cached_property
    def pet_api(self) -> PetApi:
        return PetApi(self._raw_client, self._server, self._auth)

    @cached_property
    def store(self) -> Store:
        return Store(self._raw_client, self._server, self._auth)

    @cached_property
    def user_api(self) -> UserApi:
        return UserApi(self._raw_client, self._server)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = SwaggerPetstoreOpenApi30Client
