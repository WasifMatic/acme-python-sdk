from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.delete_order_error import DeleteOrderErrorBody, delete_order_error_mapper
from ..errors.get_order_by_id_error import GetOrderByIdErrorBody, get_order_by_id_error_mapper
from ..errors.place_order_error import PlaceOrderErrorBody, place_order_error_mapper
from ..models.enums.order_status import OrderStatusOrStr
from ..models.order import Order
from ..server.server import Server


class Store:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StoreWithRawResponse(client, server, auth)

    def delete_order(self, order_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API
        errors.

        Args:
            order_id: ID of the order that needs to be deleted
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            order deleted

        Raises:
            ApiError: Invalid ID supplied Order not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_order(order_id, request_options=request_options).unwrap()

    def get_inventory(self, *, request_options: RequestOptionsOrDict | None = None) -> dict[str, int]:
        """Returns a map of status codes to quantities.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_inventory(request_options=request_options).unwrap()

    def get_order_by_id(self, order_id: int, *, request_options: RequestOptionsOrDict | None = None) -> Order:
        """For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        Args:
            order_id: ID of order that needs to be fetched
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid ID supplied Order not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_order_by_id(order_id, request_options=request_options).unwrap()

    def place_order(
        self,
        *,
        id: int | None = None,
        pet_id: int | None = None,
        quantity: int | None = None,
        ship_date: RFC3339DateTime | None = None,
        status: OrderStatusOrStr | None = None,
        complete: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Place a new order in the store.

        Args:
            id: Value sent with the request.
            pet_id: Value sent with the request.
            quantity: Value sent with the request.
            ship_date: Value sent with the request.
            status: Order Status
            complete: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid input Validation exception ``error`` is ``RawError``."""
        return self._with_raw_response.place_order(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> StoreWithRawResponse:
        return self._with_raw_response


class AsyncStore:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStoreWithRawResponse(client, server, auth)

    async def delete_order(self, order_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API
        errors.

        Args:
            order_id: ID of the order that needs to be deleted
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            order deleted

        Raises:
            ApiError: Invalid ID supplied Order not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_order(order_id, request_options=request_options)).unwrap()

    async def get_inventory(self, *, request_options: RequestOptionsOrDict | None = None) -> dict[str, int]:
        """Returns a map of status codes to quantities.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_inventory(request_options=request_options)).unwrap()

    async def get_order_by_id(self, order_id: int, *, request_options: RequestOptionsOrDict | None = None) -> Order:
        """For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        Args:
            order_id: ID of order that needs to be fetched
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid ID supplied Order not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_order_by_id(order_id, request_options=request_options)).unwrap()

    async def place_order(
        self,
        *,
        id: int | None = None,
        pet_id: int | None = None,
        quantity: int | None = None,
        ship_date: RFC3339DateTime | None = None,
        status: OrderStatusOrStr | None = None,
        complete: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Place a new order in the store.

        Args:
            id: Value sent with the request.
            pet_id: Value sent with the request.
            quantity: Value sent with the request.
            ship_date: Value sent with the request.
            status: Order Status
            complete: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid input Validation exception ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.place_order(
                id=id,
                pet_id=pet_id,
                quantity=quantity,
                ship_date=ship_date,
                status=status,
                complete=complete,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStoreWithRawResponse:
        return self._with_raw_response


class StoreWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_order(
        self, order_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteOrderErrorBody]:
        """For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API
        errors.

        Args:
            order_id: ID of the order that needs to be deleted
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/store/order/{orderId}"),
            path_params=[param[int]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_order_error_mapper,
            request_options=request_options,
        )

    def get_inventory(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[dict[str, int], RawError]:
        """Returns a map of status codes to quantities.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/store/inventory"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[dict[str, int]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_order_by_id(
        self, order_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Order, GetOrderByIdErrorBody]:
        """For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        Args:
            order_id: ID of order that needs to be fetched
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/store/order/{orderId}"),
            path_params=[param[int]("orderId", order_id)],
            decoder=json_decoder[Order],
            error_mapper=get_order_by_id_error_mapper,
            request_options=request_options,
        )

    def place_order(
        self,
        *,
        id: int | None = None,
        pet_id: int | None = None,
        quantity: int | None = None,
        ship_date: RFC3339DateTime | None = None,
        status: OrderStatusOrStr | None = None,
        complete: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, PlaceOrderErrorBody]:
        """Place a new order in the store.

        Args:
            id: Value sent with the request.
            pet_id: Value sent with the request.
            quantity: Value sent with the request.
            ship_date: Value sent with the request.
            status: Order Status
            complete: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/store/order"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[int | None]("id", id),
                param[int | None]("petId", pet_id),
                param[int | None]("quantity", quantity),
                param[RFC3339DateTime | None]("shipDate", ship_date),
                param[OrderStatusOrStr | None]("status", status),
                param[bool | None]("complete", complete),
            ),
            decoder=json_decoder[Order],
            error_mapper=place_order_error_mapper,
            request_options=request_options,
        )


class AsyncStoreWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_order(
        self, order_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteOrderErrorBody]:
        """For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API
        errors.

        Args:
            order_id: ID of the order that needs to be deleted
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/store/order/{orderId}"),
            path_params=[param[int]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_order_error_mapper,
            request_options=request_options,
        )

    async def get_inventory(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[dict[str, int], RawError]:
        """Returns a map of status codes to quantities.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/store/inventory"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[dict[str, int]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_order_by_id(
        self, order_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Order, GetOrderByIdErrorBody]:
        """For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        Args:
            order_id: ID of order that needs to be fetched
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/store/order/{orderId}"),
            path_params=[param[int]("orderId", order_id)],
            decoder=json_decoder[Order],
            error_mapper=get_order_by_id_error_mapper,
            request_options=request_options,
        )

    async def place_order(
        self,
        *,
        id: int | None = None,
        pet_id: int | None = None,
        quantity: int | None = None,
        ship_date: RFC3339DateTime | None = None,
        status: OrderStatusOrStr | None = None,
        complete: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, PlaceOrderErrorBody]:
        """Place a new order in the store.

        Args:
            id: Value sent with the request.
            pet_id: Value sent with the request.
            quantity: Value sent with the request.
            ship_date: Value sent with the request.
            status: Order Status
            complete: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/store/order"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[int | None]("id", id),
                param[int | None]("petId", pet_id),
                param[int | None]("quantity", quantity),
                param[RFC3339DateTime | None]("shipDate", ship_date),
                param[OrderStatusOrStr | None]("status", status),
                param[bool | None]("complete", complete),
            ),
            decoder=json_decoder[Order],
            error_mapper=place_order_error_mapper,
            request_options=request_options,
        )
