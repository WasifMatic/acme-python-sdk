from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncFileInput,
    AsyncRawClient,
    FileInput,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    binary_body,
    empty_response,
    form_body,
    json_decoder,
    param,
)
from ..errors.add_pet_error import AddPetErrorBody, add_pet_error_mapper
from ..errors.delete_pet_error import DeletePetErrorBody, delete_pet_error_mapper
from ..errors.find_pets_by_status_error import FindPetsByStatusErrorBody, find_pets_by_status_error_mapper
from ..errors.find_pets_by_tags_error import FindPetsByTagsErrorBody, find_pets_by_tags_error_mapper
from ..errors.get_pet_by_id_error import GetPetByIdErrorBody, get_pet_by_id_error_mapper
from ..errors.update_pet_error import UpdatePetErrorBody, update_pet_error_mapper
from ..errors.update_pet_with_form_error import UpdatePetWithFormErrorBody, update_pet_with_form_error_mapper
from ..errors.upload_file_error import UploadFileErrorBody, upload_file_error_mapper
from ..models.api_response import ApiResponse
from ..models.category import Category, CategoryDict
from ..models.enums.pet_status import PetStatusOrStr
from ..models.pet import Pet
from ..models.tag import Tag, TagDict
from ..server.server import Server


class PetApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PetApiWithRawResponse(client, server, auth)

    def add_pet(
        self,
        name: str,
        photo_urls: list[str],
        *,
        id: int | None = None,
        category: Category | CategoryDict | None = None,
        tags: list[Tag | TagDict] | None = None,
        status: PetStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pet:
        """Add a new pet to the store.

        Args:
            name: Value sent with the request.
            photo_urls: Value sent with the request.
            id: Value sent with the request.
            category: Value sent with the request.
            tags: Value sent with the request.
            status: pet status in the store
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: Invalid input Validation exception ``error`` is ``RawError``."""
        return self._with_raw_response.add_pet(
            name, photo_urls, id=id, category=category, tags=tags, status=status, request_options=request_options
        ).unwrap()

    def delete_pet(
        self, pet_id: int, *, api_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a pet.

        Args:
            pet_id: Pet id to delete
            api_key: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pet deleted

        Raises:
            ApiError: Invalid pet value ``error`` is ``RawError``."""
        return self._with_raw_response.delete_pet(pet_id, api_key=api_key, request_options=request_options).unwrap()

    def find_pets_by_status(
        self, *, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[Pet]:
        """Multiple status values can be provided with comma separated strings.

        Args:
            status: Status values that need to be considered for filter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid status value ``error`` is ``RawError``."""
        return self._with_raw_response.find_pets_by_status(status=status, request_options=request_options).unwrap()

    def find_pets_by_tags(
        self, *, tags: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[Pet]:
        """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        Args:
            tags: Tags to filter by
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid tag value ``error`` is ``RawError``."""
        return self._with_raw_response.find_pets_by_tags(tags=tags, request_options=request_options).unwrap()

    def get_pet_by_id(self, pet_id: int, *, request_options: RequestOptionsOrDict | None = None) -> Pet:
        """Returns a single pet.

        Args:
            pet_id: ID of pet to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid ID supplied Pet not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_pet_by_id(pet_id, request_options=request_options).unwrap()

    def update_pet(
        self,
        name: str,
        photo_urls: list[str],
        *,
        id: int | None = None,
        category: Category | CategoryDict | None = None,
        tags: list[Tag | TagDict] | None = None,
        status: PetStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pet:
        """Update an existing pet by Id.

        Args:
            name: Value sent with the request.
            photo_urls: Value sent with the request.
            id: Value sent with the request.
            category: Value sent with the request.
            tags: Value sent with the request.
            status: pet status in the store
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: Invalid ID supplied Pet not found Validation exception ``error`` is ``RawError``."""
        return self._with_raw_response.update_pet(
            name, photo_urls, id=id, category=category, tags=tags, status=status, request_options=request_options
        ).unwrap()

    def update_pet_with_form(
        self,
        pet_id: int,
        *,
        name: str | None = None,
        status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pet:
        """Updates a pet resource based on the form data.

        Args:
            pet_id: ID of pet that needs to be updated
            name: Name of pet that needs to be updated
            status: Status of pet that needs to be updated
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid input ``error`` is ``RawError``."""
        return self._with_raw_response.update_pet_with_form(
            pet_id, name=name, status=status, request_options=request_options
        ).unwrap()

    def upload_file(
        self,
        pet_id: int,
        *,
        additional_metadata: str | None = None,
        body: FileInput | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResponse:
        """Upload image of the pet.

        Args:
            pet_id: ID of pet to update
            additional_metadata: Additional Metadata
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: No file uploaded Pet not found ``error`` is ``RawError``."""
        return self._with_raw_response.upload_file(
            pet_id, additional_metadata=additional_metadata, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PetApiWithRawResponse:
        return self._with_raw_response


class AsyncPetApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPetApiWithRawResponse(client, server, auth)

    async def add_pet(
        self,
        name: str,
        photo_urls: list[str],
        *,
        id: int | None = None,
        category: Category | CategoryDict | None = None,
        tags: list[Tag | TagDict] | None = None,
        status: PetStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pet:
        """Add a new pet to the store.

        Args:
            name: Value sent with the request.
            photo_urls: Value sent with the request.
            id: Value sent with the request.
            category: Value sent with the request.
            tags: Value sent with the request.
            status: pet status in the store
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: Invalid input Validation exception ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_pet(
                name, photo_urls, id=id, category=category, tags=tags, status=status, request_options=request_options
            )
        ).unwrap()

    async def delete_pet(
        self, pet_id: int, *, api_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a pet.

        Args:
            pet_id: Pet id to delete
            api_key: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pet deleted

        Raises:
            ApiError: Invalid pet value ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_pet(pet_id, api_key=api_key, request_options=request_options)
        ).unwrap()

    async def find_pets_by_status(
        self, *, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[Pet]:
        """Multiple status values can be provided with comma separated strings.

        Args:
            status: Status values that need to be considered for filter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid status value ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.find_pets_by_status(status=status, request_options=request_options)
        ).unwrap()

    async def find_pets_by_tags(
        self, *, tags: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[Pet]:
        """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        Args:
            tags: Tags to filter by
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid tag value ``error`` is ``RawError``."""
        return (await self._with_raw_response.find_pets_by_tags(tags=tags, request_options=request_options)).unwrap()

    async def get_pet_by_id(self, pet_id: int, *, request_options: RequestOptionsOrDict | None = None) -> Pet:
        """Returns a single pet.

        Args:
            pet_id: ID of pet to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid ID supplied Pet not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_pet_by_id(pet_id, request_options=request_options)).unwrap()

    async def update_pet(
        self,
        name: str,
        photo_urls: list[str],
        *,
        id: int | None = None,
        category: Category | CategoryDict | None = None,
        tags: list[Tag | TagDict] | None = None,
        status: PetStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pet:
        """Update an existing pet by Id.

        Args:
            name: Value sent with the request.
            photo_urls: Value sent with the request.
            id: Value sent with the request.
            category: Value sent with the request.
            tags: Value sent with the request.
            status: pet status in the store
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: Invalid ID supplied Pet not found Validation exception ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_pet(
                name, photo_urls, id=id, category=category, tags=tags, status=status, request_options=request_options
            )
        ).unwrap()

    async def update_pet_with_form(
        self,
        pet_id: int,
        *,
        name: str | None = None,
        status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pet:
        """Updates a pet resource based on the form data.

        Args:
            pet_id: ID of pet that needs to be updated
            name: Name of pet that needs to be updated
            status: Status of pet that needs to be updated
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: Invalid input ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_pet_with_form(
                pet_id, name=name, status=status, request_options=request_options
            )
        ).unwrap()

    async def upload_file(
        self,
        pet_id: int,
        *,
        additional_metadata: str | None = None,
        body: AsyncFileInput | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResponse:
        """Upload image of the pet.

        Args:
            pet_id: ID of pet to update
            additional_metadata: Additional Metadata
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: No file uploaded Pet not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.upload_file(
                pet_id, additional_metadata=additional_metadata, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPetApiWithRawResponse:
        return self._with_raw_response


class PetApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_pet(
        self,
        name: str,
        photo_urls: list[str],
        *,
        id: int | None = None,
        category: Category | CategoryDict | None = None,
        tags: list[Tag | TagDict] | None = None,
        status: PetStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pet, AddPetErrorBody]:
        """Add a new pet to the store.

        Args:
            name: Value sent with the request.
            photo_urls: Value sent with the request.
            id: Value sent with the request.
            category: Value sent with the request.
            tags: Value sent with the request.
            status: pet status in the store
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pet"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[str]("name", name),
                param[list[str]]("photoUrls", photo_urls),
                param[int | None]("id", id),
                param[Category | CategoryDict | None]("category", category),
                param[list[Tag | TagDict] | None]("tags", tags),
                param[PetStatusOrStr | None]("status", status),
            ),
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[Pet],
            error_mapper=add_pet_error_mapper,
            request_options=request_options,
        )

    def delete_pet(
        self, pet_id: int, *, api_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeletePetErrorBody]:
        """Delete a pet.

        Args:
            pet_id: Pet id to delete
            api_key: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/pet/{petId}"),
            path_params=[param[int]("petId", pet_id)],
            headers=[param[str | None]("api_key", api_key), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.petstore_auth,
            decoder=empty_response,
            error_mapper=delete_pet_error_mapper,
            request_options=request_options,
        )

    def find_pets_by_status(
        self, *, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Pet], FindPetsByStatusErrorBody]:
        """Multiple status values can be provided with comma separated strings.

        Args:
            status: Status values that need to be considered for filter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/pet/findByStatus"),
            query_params=[param[PetStatusOrStr | None]("status", status)],
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[list[Pet]],
            error_mapper=find_pets_by_status_error_mapper,
            request_options=request_options,
        )

    def find_pets_by_tags(
        self, *, tags: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Pet], FindPetsByTagsErrorBody]:
        """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        Args:
            tags: Tags to filter by
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/pet/findByTags"),
            query_params=[param[list[str] | None]("tags", tags)],
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[list[Pet]],
            error_mapper=find_pets_by_tags_error_mapper,
            request_options=request_options,
        )

    def get_pet_by_id(
        self, pet_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Pet, GetPetByIdErrorBody]:
        """Returns a single pet.

        Args:
            pet_id: ID of pet to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/pet/{petId}"),
            path_params=[param[int]("petId", pet_id)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.petstore_auth),
            decoder=json_decoder[Pet],
            error_mapper=get_pet_by_id_error_mapper,
            request_options=request_options,
        )

    def update_pet(
        self,
        name: str,
        photo_urls: list[str],
        *,
        id: int | None = None,
        category: Category | CategoryDict | None = None,
        tags: list[Tag | TagDict] | None = None,
        status: PetStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pet, UpdatePetErrorBody]:
        """Update an existing pet by Id.

        Args:
            name: Value sent with the request.
            photo_urls: Value sent with the request.
            id: Value sent with the request.
            category: Value sent with the request.
            tags: Value sent with the request.
            status: pet status in the store
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/pet"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[str]("name", name),
                param[list[str]]("photoUrls", photo_urls),
                param[int | None]("id", id),
                param[Category | CategoryDict | None]("category", category),
                param[list[Tag | TagDict] | None]("tags", tags),
                param[PetStatusOrStr | None]("status", status),
            ),
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[Pet],
            error_mapper=update_pet_error_mapper,
            request_options=request_options,
        )

    def update_pet_with_form(
        self,
        pet_id: int,
        *,
        name: str | None = None,
        status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pet, UpdatePetWithFormErrorBody]:
        """Updates a pet resource based on the form data.

        Args:
            pet_id: ID of pet that needs to be updated
            name: Name of pet that needs to be updated
            status: Status of pet that needs to be updated
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pet/{petId}"),
            path_params=[param[int]("petId", pet_id)],
            query_params=[param[str | None]("name", name), param[str | None]("status", status)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[Pet],
            error_mapper=update_pet_with_form_error_mapper,
            request_options=request_options,
        )

    def upload_file(
        self,
        pet_id: int,
        *,
        additional_metadata: str | None = None,
        body: FileInput | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiResponse, UploadFileErrorBody]:
        """Upload image of the pet.

        Args:
            pet_id: ID of pet to update
            additional_metadata: Additional Metadata
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pet/{petId}/uploadImage"),
            path_params=[param[int]("petId", pet_id)],
            query_params=[param[str | None]("additionalMetadata", additional_metadata)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=binary_body(body),
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[ApiResponse],
            error_mapper=upload_file_error_mapper,
            request_options=request_options,
        )


class AsyncPetApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_pet(
        self,
        name: str,
        photo_urls: list[str],
        *,
        id: int | None = None,
        category: Category | CategoryDict | None = None,
        tags: list[Tag | TagDict] | None = None,
        status: PetStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pet, AddPetErrorBody]:
        """Add a new pet to the store.

        Args:
            name: Value sent with the request.
            photo_urls: Value sent with the request.
            id: Value sent with the request.
            category: Value sent with the request.
            tags: Value sent with the request.
            status: pet status in the store
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pet"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[str]("name", name),
                param[list[str]]("photoUrls", photo_urls),
                param[int | None]("id", id),
                param[Category | CategoryDict | None]("category", category),
                param[list[Tag | TagDict] | None]("tags", tags),
                param[PetStatusOrStr | None]("status", status),
            ),
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[Pet],
            error_mapper=add_pet_error_mapper,
            request_options=request_options,
        )

    async def delete_pet(
        self, pet_id: int, *, api_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeletePetErrorBody]:
        """Delete a pet.

        Args:
            pet_id: Pet id to delete
            api_key: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/pet/{petId}"),
            path_params=[param[int]("petId", pet_id)],
            headers=[param[str | None]("api_key", api_key), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.petstore_auth,
            decoder=empty_response,
            error_mapper=delete_pet_error_mapper,
            request_options=request_options,
        )

    async def find_pets_by_status(
        self, *, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Pet], FindPetsByStatusErrorBody]:
        """Multiple status values can be provided with comma separated strings.

        Args:
            status: Status values that need to be considered for filter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/pet/findByStatus"),
            query_params=[param[PetStatusOrStr | None]("status", status)],
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[list[Pet]],
            error_mapper=find_pets_by_status_error_mapper,
            request_options=request_options,
        )

    async def find_pets_by_tags(
        self, *, tags: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Pet], FindPetsByTagsErrorBody]:
        """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        Args:
            tags: Tags to filter by
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/pet/findByTags"),
            query_params=[param[list[str] | None]("tags", tags)],
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[list[Pet]],
            error_mapper=find_pets_by_tags_error_mapper,
            request_options=request_options,
        )

    async def get_pet_by_id(
        self, pet_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Pet, GetPetByIdErrorBody]:
        """Returns a single pet.

        Args:
            pet_id: ID of pet to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/pet/{petId}"),
            path_params=[param[int]("petId", pet_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.petstore_auth),
            decoder=json_decoder[Pet],
            error_mapper=get_pet_by_id_error_mapper,
            request_options=request_options,
        )

    async def update_pet(
        self,
        name: str,
        photo_urls: list[str],
        *,
        id: int | None = None,
        category: Category | CategoryDict | None = None,
        tags: list[Tag | TagDict] | None = None,
        status: PetStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pet, UpdatePetErrorBody]:
        """Update an existing pet by Id.

        Args:
            name: Value sent with the request.
            photo_urls: Value sent with the request.
            id: Value sent with the request.
            category: Value sent with the request.
            tags: Value sent with the request.
            status: pet status in the store
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/pet"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[str]("name", name),
                param[list[str]]("photoUrls", photo_urls),
                param[int | None]("id", id),
                param[Category | CategoryDict | None]("category", category),
                param[list[Tag | TagDict] | None]("tags", tags),
                param[PetStatusOrStr | None]("status", status),
            ),
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[Pet],
            error_mapper=update_pet_error_mapper,
            request_options=request_options,
        )

    async def update_pet_with_form(
        self,
        pet_id: int,
        *,
        name: str | None = None,
        status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pet, UpdatePetWithFormErrorBody]:
        """Updates a pet resource based on the form data.

        Args:
            pet_id: ID of pet that needs to be updated
            name: Name of pet that needs to be updated
            status: Status of pet that needs to be updated
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pet/{petId}"),
            path_params=[param[int]("petId", pet_id)],
            query_params=[param[str | None]("name", name), param[str | None]("status", status)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[Pet],
            error_mapper=update_pet_with_form_error_mapper,
            request_options=request_options,
        )

    async def upload_file(
        self,
        pet_id: int,
        *,
        additional_metadata: str | None = None,
        body: AsyncFileInput | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiResponse, UploadFileErrorBody]:
        """Upload image of the pet.

        Args:
            pet_id: ID of pet to update
            additional_metadata: Additional Metadata
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pet/{petId}/uploadImage"),
            path_params=[param[int]("petId", pet_id)],
            query_params=[param[str | None]("additionalMetadata", additional_metadata)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=binary_body(body),
            auth_scheme=self._auth.petstore_auth,
            decoder=json_decoder[ApiResponse],
            error_mapper=upload_file_error_mapper,
            request_options=request_options,
        )
