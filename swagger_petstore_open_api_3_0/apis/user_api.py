from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    empty_response,
    form_body,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.delete_user_error import DeleteUserErrorBody, delete_user_error_mapper
from ..errors.get_user_by_name_error import GetUserByNameErrorBody, get_user_by_name_error_mapper
from ..errors.login_user_error import LoginUserErrorBody, login_user_error_mapper
from ..errors.update_user_error import UpdateUserErrorBody, update_user_error_mapper
from ..models.user import User, UserDict
from ..server.server import Server


class UserApi:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = UserApiWithRawResponse(client, server)

    def create_user(
        self,
        *,
        id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone: str | None = None,
        user_status: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> User:
        """This can only be done by the logged in user.

        Args:
            id: Value sent with the request.
            username: Value sent with the request.
            first_name: Value sent with the request.
            last_name: Value sent with the request.
            email: Value sent with the request.
            password: Value sent with the request.
            phone: Value sent with the request.
            user_status: User Status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_user(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone,
            user_status=user_status,
            request_options=request_options,
        ).unwrap()

    def create_users_with_list_input(
        self, *, body: list[User | UserDict] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """Creates list of users with given input array.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_users_with_list_input(body=body, request_options=request_options).unwrap()

    def delete_user(self, usersname: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This can only be done by the logged in user.

        Args:
            usersname: The username that needs to be processed
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User deleted

        Raises:
            ApiError: Invalid username supplied User not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_user(usersname, request_options=request_options).unwrap()

    def get_user_by_name(self, usersname: str, *, request_options: RequestOptionsOrDict | None = None) -> User:
        """Get user detail based on username.

        Args:
            usersname: The username that needs to be processed
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid username supplied User not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_by_name(usersname, request_options=request_options).unwrap()

    def login_user(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Log into the system.

        Args:
            username: The user name for login
            password: The password for login in clear text
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid username/password supplied ``error`` is ``RawError``."""
        return self._with_raw_response.login_user(
            username=username, password=password, request_options=request_options
        ).unwrap()

    def logout_user(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Log user out of the system.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.logout_user(request_options=request_options).unwrap()

    def update_user(
        self,
        usersname: str,
        *,
        id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone: str | None = None,
        user_status: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This can only be done by the logged in user.

        Args:
            usersname: The username that needs to be processed
            id: Value sent with the request.
            username: Value sent with the request.
            first_name: Value sent with the request.
            last_name: Value sent with the request.
            email: Value sent with the request.
            password: Value sent with the request.
            phone: Value sent with the request.
            user_status: User Status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: bad request user not found ``error`` is ``RawError``."""
        return self._with_raw_response.update_user(
            usersname,
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone,
            user_status=user_status,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> UserApiWithRawResponse:
        return self._with_raw_response


class AsyncUserApi:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncUserApiWithRawResponse(client, server)

    async def create_user(
        self,
        *,
        id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone: str | None = None,
        user_status: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> User:
        """This can only be done by the logged in user.

        Args:
            id: Value sent with the request.
            username: Value sent with the request.
            first_name: Value sent with the request.
            last_name: Value sent with the request.
            email: Value sent with the request.
            password: Value sent with the request.
            phone: Value sent with the request.
            user_status: User Status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_user(
                id=id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                phone=phone,
                user_status=user_status,
                request_options=request_options,
            )
        ).unwrap()

    async def create_users_with_list_input(
        self, *, body: list[User | UserDict] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """Creates list of users with given input array.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_users_with_list_input(body=body, request_options=request_options)
        ).unwrap()

    async def delete_user(self, usersname: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This can only be done by the logged in user.

        Args:
            usersname: The username that needs to be processed
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User deleted

        Raises:
            ApiError: Invalid username supplied User not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_user(usersname, request_options=request_options)).unwrap()

    async def get_user_by_name(self, usersname: str, *, request_options: RequestOptionsOrDict | None = None) -> User:
        """Get user detail based on username.

        Args:
            usersname: The username that needs to be processed
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid username supplied User not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_user_by_name(usersname, request_options=request_options)).unwrap()

    async def login_user(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Log into the system.

        Args:
            username: The user name for login
            password: The password for login in clear text
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid username/password supplied ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.login_user(
                username=username, password=password, request_options=request_options
            )
        ).unwrap()

    async def logout_user(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Log user out of the system.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.logout_user(request_options=request_options)).unwrap()

    async def update_user(
        self,
        usersname: str,
        *,
        id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone: str | None = None,
        user_status: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This can only be done by the logged in user.

        Args:
            usersname: The username that needs to be processed
            id: Value sent with the request.
            username: Value sent with the request.
            first_name: Value sent with the request.
            last_name: Value sent with the request.
            email: Value sent with the request.
            password: Value sent with the request.
            phone: Value sent with the request.
            user_status: User Status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: bad request user not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_user(
                usersname,
                id=id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                phone=phone,
                user_status=user_status,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUserApiWithRawResponse:
        return self._with_raw_response


class UserApiWithRawResponse(BaseRawResponse[RawClient, Server]):
    def create_user(
        self,
        *,
        id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone: str | None = None,
        user_status: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[User, RawError]:
        """This can only be done by the logged in user.

        Args:
            id: Value sent with the request.
            username: Value sent with the request.
            first_name: Value sent with the request.
            last_name: Value sent with the request.
            email: Value sent with the request.
            password: Value sent with the request.
            phone: Value sent with the request.
            user_status: User Status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/user"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[int | None]("id", id),
                param[str | None]("username", username),
                param[str | None]("firstName", first_name),
                param[str | None]("lastName", last_name),
                param[str | None]("email", email),
                param[str | None]("password", password),
                param[str | None]("phone", phone),
                param[int | None]("userStatus", user_status),
            ),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_users_with_list_input(
        self, *, body: list[User | UserDict] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, RawError]:
        """Creates list of users with given input array.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/user/createWithList"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[User | UserDict] | None](body),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_user(
        self, usersname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteUserErrorBody]:
        """This can only be done by the logged in user.

        Args:
            usersname: The username that needs to be processed
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/user/{usersname}"),
            path_params=[param[str]("usersname", usersname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_user_error_mapper,
            request_options=request_options,
        )

    def get_user_by_name(
        self, usersname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, GetUserByNameErrorBody]:
        """Get user detail based on username.

        Args:
            usersname: The username that needs to be processed
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user/{usersname}"),
            path_params=[param[str]("usersname", usersname)],
            decoder=json_decoder[User],
            error_mapper=get_user_by_name_error_mapper,
            request_options=request_options,
        )

    def login_user(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, LoginUserErrorBody]:
        """Log into the system.

        Args:
            username: The user name for login
            password: The password for login in clear text
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user/login"),
            query_params=[param[str | None]("username", username), param[str | None]("password", password)],
            decoder=empty_response,
            error_mapper=login_user_error_mapper,
            request_options=request_options,
        )

    def logout_user(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]:
        """Log user out of the system.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user/logout"),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_user(
        self,
        usersname: str,
        *,
        id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone: str | None = None,
        user_status: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateUserErrorBody]:
        """This can only be done by the logged in user.

        Args:
            usersname: The username that needs to be processed
            id: Value sent with the request.
            username: Value sent with the request.
            first_name: Value sent with the request.
            last_name: Value sent with the request.
            email: Value sent with the request.
            password: Value sent with the request.
            phone: Value sent with the request.
            user_status: User Status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/user/{usersname}"),
            path_params=[param[str]("usersname", usersname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[int | None]("id", id),
                param[str | None]("username", username),
                param[str | None]("firstName", first_name),
                param[str | None]("lastName", last_name),
                param[str | None]("email", email),
                param[str | None]("password", password),
                param[str | None]("phone", phone),
                param[int | None]("userStatus", user_status),
            ),
            decoder=empty_response,
            error_mapper=update_user_error_mapper,
            request_options=request_options,
        )


class AsyncUserApiWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def create_user(
        self,
        *,
        id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone: str | None = None,
        user_status: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[User, RawError]:
        """This can only be done by the logged in user.

        Args:
            id: Value sent with the request.
            username: Value sent with the request.
            first_name: Value sent with the request.
            last_name: Value sent with the request.
            email: Value sent with the request.
            password: Value sent with the request.
            phone: Value sent with the request.
            user_status: User Status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/user"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[int | None]("id", id),
                param[str | None]("username", username),
                param[str | None]("firstName", first_name),
                param[str | None]("lastName", last_name),
                param[str | None]("email", email),
                param[str | None]("password", password),
                param[str | None]("phone", phone),
                param[int | None]("userStatus", user_status),
            ),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_users_with_list_input(
        self, *, body: list[User | UserDict] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, RawError]:
        """Creates list of users with given input array.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/user/createWithList"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[User | UserDict] | None](body),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_user(
        self, usersname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteUserErrorBody]:
        """This can only be done by the logged in user.

        Args:
            usersname: The username that needs to be processed
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/user/{usersname}"),
            path_params=[param[str]("usersname", usersname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_user_error_mapper,
            request_options=request_options,
        )

    async def get_user_by_name(
        self, usersname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, GetUserByNameErrorBody]:
        """Get user detail based on username.

        Args:
            usersname: The username that needs to be processed
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user/{usersname}"),
            path_params=[param[str]("usersname", usersname)],
            decoder=json_decoder[User],
            error_mapper=get_user_by_name_error_mapper,
            request_options=request_options,
        )

    async def login_user(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, LoginUserErrorBody]:
        """Log into the system.

        Args:
            username: The user name for login
            password: The password for login in clear text
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user/login"),
            query_params=[param[str | None]("username", username), param[str | None]("password", password)],
            decoder=empty_response,
            error_mapper=login_user_error_mapper,
            request_options=request_options,
        )

    async def logout_user(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]:
        """Log user out of the system.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user/logout"),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_user(
        self,
        usersname: str,
        *,
        id: int | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        phone: str | None = None,
        user_status: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateUserErrorBody]:
        """This can only be done by the logged in user.

        Args:
            usersname: The username that needs to be processed
            id: Value sent with the request.
            username: Value sent with the request.
            first_name: Value sent with the request.
            last_name: Value sent with the request.
            email: Value sent with the request.
            password: Value sent with the request.
            phone: Value sent with the request.
            user_status: User Status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/user/{usersname}"),
            path_params=[param[str]("usersname", usersname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[int | None]("id", id),
                param[str | None]("username", username),
                param[str | None]("firstName", first_name),
                param[str | None]("lastName", last_name),
                param[str | None]("email", email),
                param[str | None]("password", password),
                param[str | None]("phone", phone),
                param[int | None]("userStatus", user_status),
            ),
            decoder=empty_response,
            error_mapper=update_user_error_mapper,
            request_options=request_options,
        )
