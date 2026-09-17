from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.pet_api import AsyncPetApi
from .apis.store import AsyncStore
from .apis.user_api import AsyncUserApi
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseSwaggerPetstoreOpenApi30Client
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    no_auth,
    param,
)
from .server.server_config import ServerConfigOrDict


class AsyncSwaggerPetstoreOpenApi30Client(BaseSwaggerPetstoreOpenApi30Client[AsyncRawClient]):
    def __init__(
        self,
        *,
        server_config: ServerConfigOrDict | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        petstore_auth: str | None = None,
        api_key: str | None = None,
    ) -> None:
        super().__init__(server_config=server_config, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "SwaggerPetstoreOpenApi30Client/1.0.26 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.26"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            petstore_auth=ApiKeyHeaderScheme("Authorization", petstore_auth) if petstore_auth is not None else no_auth,
            api_key=ApiKeyHeaderScheme("api_key", api_key) if api_key is not None else no_auth,
        )

    @cached_property
    def pet_api(self) -> AsyncPetApi:
        return AsyncPetApi(self._raw_client, self._server, self._auth)

    @cached_property
    def store(self) -> AsyncStore:
        return AsyncStore(self._raw_client, self._server, self._auth)

    @cached_property
    def user_api(self) -> AsyncUserApi:
        return AsyncUserApi(self._raw_client, self._server)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncSwaggerPetstoreOpenApi30Client
