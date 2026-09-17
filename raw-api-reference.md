# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [SwaggerPetstoreOpenApi30Client](swagger_petstore_open_api_3_0/client.py)

## PetApi

> Source: [PetApi](swagger_petstore_open_api_3_0/apis/pet_api.py)

<details>
<summary><code>def add_pet(name: str, photo_urls: list[str], *, id: int | None = None, category: Category | CategoryDict | None = None, tags: list[TagModel | TagModelDict] | None = None, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Pet, AddPetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add a new pet to the store.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pet_api.with_raw_response.add_pet(name, photo_urls)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Pet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddPetErrorBody
```

**Async**

```python
result = await async_client.pet_api.with_raw_response.add_pet(name, photo_urls)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Pet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddPetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | Value sent with the request. |
| <code>photo_urls</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>category</code> | <code>[Category](swagger_petstore_open_api_3_0/models/category.py) \| [CategoryDict](swagger_petstore_open_api_3_0/models/category.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>tags</code> | <code>list&#91;[TagModel](swagger_petstore_open_api_3_0/models/tag_model.py) \| [TagModelDict](swagger_petstore_open_api_3_0/models/tag_model.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[PetStatusOrStr](swagger_petstore_open_api_3_0/models/enums/pet_status.py) \| None</code> | pet status in the store<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[Pet](swagger_petstore_open_api_3_0/models/pet.py), [AddPetErrorBody](swagger_petstore_open_api_3_0/errors/add_pet_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Pet](swagger_petstore_open_api_3_0/models/pet.py)</code> -- Successful operation

**On `Failure`**: `error` is <code>[AddPetErrorBody](swagger_petstore_open_api_3_0/errors/add_pet_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 422 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_pet(pet_id: int, *, api_key: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeletePetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete a pet.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pet_api.with_raw_response.delete_pet(pet_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeletePetErrorBody
```

**Async**

```python
result = await async_client.pet_api.with_raw_response.delete_pet(pet_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeletePetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>pet_id</code> | <code>int</code> | Pet id to delete |
| <code>api_key</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;None, [DeletePetErrorBody](swagger_petstore_open_api_3_0/errors/delete_pet_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeletePetErrorBody](swagger_petstore_open_api_3_0/errors/delete_pet_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_pets_by_status(*, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Pet], FindPetsByStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Multiple status values can be provided with comma separated strings.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pet_api.with_raw_response.find_pets_by_status()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Pet]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FindPetsByStatusErrorBody
```

**Async**

```python
result = await async_client.pet_api.with_raw_response.find_pets_by_status()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Pet]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FindPetsByStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>status</code> | <code>[PetStatusOrStr](swagger_petstore_open_api_3_0/models/enums/pet_status.py) \| None</code> | Status values that need to be considered for filter<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;list&#91;[Pet](swagger_petstore_open_api_3_0/models/pet.py)&#93;, [FindPetsByStatusErrorBody](swagger_petstore_open_api_3_0/errors/find_pets_by_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Pet](swagger_petstore_open_api_3_0/models/pet.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[FindPetsByStatusErrorBody](swagger_petstore_open_api_3_0/errors/find_pets_by_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_pets_by_tags(*, tags: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Pet], FindPetsByTagsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pet_api.with_raw_response.find_pets_by_tags()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Pet]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FindPetsByTagsErrorBody
```

**Async**

```python
result = await async_client.pet_api.with_raw_response.find_pets_by_tags()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Pet]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FindPetsByTagsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>tags</code> | <code>list&#91;str&#93; \| None</code> | Tags to filter by<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;list&#91;[Pet](swagger_petstore_open_api_3_0/models/pet.py)&#93;, [FindPetsByTagsErrorBody](swagger_petstore_open_api_3_0/errors/find_pets_by_tags_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Pet](swagger_petstore_open_api_3_0/models/pet.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[FindPetsByTagsErrorBody](swagger_petstore_open_api_3_0/errors/find_pets_by_tags_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_pet_by_id(pet_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Pet, GetPetByIdErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single pet.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pet_api.with_raw_response.get_pet_by_id(pet_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Pet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPetByIdErrorBody
```

**Async**

```python
result = await async_client.pet_api.with_raw_response.get_pet_by_id(pet_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Pet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPetByIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>pet_id</code> | <code>int</code> | ID of pet to return |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[Pet](swagger_petstore_open_api_3_0/models/pet.py), [GetPetByIdErrorBody](swagger_petstore_open_api_3_0/errors/get_pet_by_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Pet](swagger_petstore_open_api_3_0/models/pet.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[GetPetByIdErrorBody](swagger_petstore_open_api_3_0/errors/get_pet_by_id_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_pet(name: str, photo_urls: list[str], *, id: int | None = None, category: Category | CategoryDict | None = None, tags: list[TagModel | TagModelDict] | None = None, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Pet, UpdatePetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update an existing pet by Id.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pet_api.with_raw_response.update_pet(name, photo_urls)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Pet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdatePetErrorBody
```

**Async**

```python
result = await async_client.pet_api.with_raw_response.update_pet(name, photo_urls)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Pet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdatePetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | Value sent with the request. |
| <code>photo_urls</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>category</code> | <code>[Category](swagger_petstore_open_api_3_0/models/category.py) \| [CategoryDict](swagger_petstore_open_api_3_0/models/category.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>tags</code> | <code>list&#91;[TagModel](swagger_petstore_open_api_3_0/models/tag_model.py) \| [TagModelDict](swagger_petstore_open_api_3_0/models/tag_model.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[PetStatusOrStr](swagger_petstore_open_api_3_0/models/enums/pet_status.py) \| None</code> | pet status in the store<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[Pet](swagger_petstore_open_api_3_0/models/pet.py), [UpdatePetErrorBody](swagger_petstore_open_api_3_0/errors/update_pet_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Pet](swagger_petstore_open_api_3_0/models/pet.py)</code> -- Successful operation

**On `Failure`**: `error` is <code>[UpdatePetErrorBody](swagger_petstore_open_api_3_0/errors/update_pet_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 422 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_pet_with_form(pet_id: int, *, name: str | None = None, status: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Pet, UpdatePetWithFormErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a pet resource based on the form data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pet_api.with_raw_response.update_pet_with_form(pet_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Pet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdatePetWithFormErrorBody
```

**Async**

```python
result = await async_client.pet_api.with_raw_response.update_pet_with_form(pet_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Pet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdatePetWithFormErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>pet_id</code> | <code>int</code> | ID of pet that needs to be updated |
| <code>name</code> | <code>str \| None</code> | Name of pet that needs to be updated<br>**Default**: <code>None</code> |
| <code>status</code> | <code>str \| None</code> | Status of pet that needs to be updated<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[Pet](swagger_petstore_open_api_3_0/models/pet.py), [UpdatePetWithFormErrorBody](swagger_petstore_open_api_3_0/errors/update_pet_with_form_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Pet](swagger_petstore_open_api_3_0/models/pet.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[UpdatePetWithFormErrorBody](swagger_petstore_open_api_3_0/errors/update_pet_with_form_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upload_file(pet_id: int, *, additional_metadata: str | None = None, body: FileInput | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ApiResponse, UploadFileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Upload image of the pet.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pet_api.with_raw_response.upload_file(pet_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UploadFileErrorBody
```

**Async**

```python
result = await async_client.pet_api.with_raw_response.upload_file(pet_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UploadFileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>pet_id</code> | <code>int</code> | ID of pet to update |
| <code>additional_metadata</code> | <code>str \| None</code> | Additional Metadata<br>**Default**: <code>None</code> |
| <code>body</code> | <code>FileInput \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[ApiResponse](swagger_petstore_open_api_3_0/models/api_response.py), [UploadFileErrorBody](swagger_petstore_open_api_3_0/errors/upload_file_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ApiResponse](swagger_petstore_open_api_3_0/models/api_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[UploadFileErrorBody](swagger_petstore_open_api_3_0/errors/upload_file_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Store

> Source: [Store](swagger_petstore_open_api_3_0/apis/store.py)

<details>
<summary><code>def delete_order(order_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteOrderErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.store.with_raw_response.delete_order(order_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteOrderErrorBody
```

**Async**

```python
result = await async_client.store.with_raw_response.delete_order(order_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>int</code> | ID of the order that needs to be deleted |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;None, [DeleteOrderErrorBody](swagger_petstore_open_api_3_0/errors/delete_order_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteOrderErrorBody](swagger_petstore_open_api_3_0/errors/delete_order_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_inventory(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[dict[str, int], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a map of status codes to quantities.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.store.with_raw_response.get_inventory()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type dict[str, int]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.store.with_raw_response.get_inventory()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type dict[str, int]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;dict&#91;str, int&#93;, [RawError](swagger_petstore_open_api_3_0/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>dict&#91;str, int&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_order_by_id(order_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Order, GetOrderByIdErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.store.with_raw_response.get_order_by_id(order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderByIdErrorBody
```

**Async**

```python
result = await async_client.store.with_raw_response.get_order_by_id(order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderByIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>int</code> | ID of order that needs to be fetched |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[Order](swagger_petstore_open_api_3_0/models/order.py), [GetOrderByIdErrorBody](swagger_petstore_open_api_3_0/errors/get_order_by_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Order](swagger_petstore_open_api_3_0/models/order.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[GetOrderByIdErrorBody](swagger_petstore_open_api_3_0/errors/get_order_by_id_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def place_order(*, id: int | None = None, pet_id: int | None = None, quantity: int | None = None, ship_date: RFC3339DateTime | None = None, status: OrderStatusOrStr | None = None, complete: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Order, PlaceOrderErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Place a new order in the store.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.store.with_raw_response.place_order()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PlaceOrderErrorBody
```

**Async**

```python
result = await async_client.store.with_raw_response.place_order()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PlaceOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pet_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>quantity</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>ship_date</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[OrderStatusOrStr](swagger_petstore_open_api_3_0/models/enums/order_status.py) \| None</code> | Order Status<br>**Default**: <code>None</code> |
| <code>complete</code> | <code>bool \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[Order](swagger_petstore_open_api_3_0/models/order.py), [PlaceOrderErrorBody](swagger_petstore_open_api_3_0/errors/place_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Order](swagger_petstore_open_api_3_0/models/order.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[PlaceOrderErrorBody](swagger_petstore_open_api_3_0/errors/place_order_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 422 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## UserApi

> Source: [UserApi](swagger_petstore_open_api_3_0/apis/user_api.py)

<details>
<summary><code>def create_user(*, id: int | None = None, username: str | None = None, first_name: str | None = None, last_name: str | None = None, email: str | None = None, password: str | None = None, phone: str | None = None, user_status: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[User, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This can only be done by the logged in user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_api.with_raw_response.create_user()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type User
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.user_api.with_raw_response.create_user()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type User
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>first_name</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>last_name</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>email</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>password</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>phone</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>user_status</code> | <code>int \| None</code> | User Status<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[User](swagger_petstore_open_api_3_0/models/user.py), [RawError](swagger_petstore_open_api_3_0/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[User](swagger_petstore_open_api_3_0/models/user.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_users_with_list_input(*, body: list[User | UserDict] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[User, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates list of users with given input array.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_api.with_raw_response.create_users_with_list_input()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type User
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.user_api.with_raw_response.create_users_with_list_input()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type User
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>list&#91;[User](swagger_petstore_open_api_3_0/models/user.py) \| [UserDict](swagger_petstore_open_api_3_0/models/user.py)&#93; \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[User](swagger_petstore_open_api_3_0/models/user.py), [RawError](swagger_petstore_open_api_3_0/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[User](swagger_petstore_open_api_3_0/models/user.py)</code> -- Successful operation

**On `Failure`**: `error` is <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_user(usersname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This can only be done by the logged in user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_api.with_raw_response.delete_user(usersname)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteUserErrorBody
```

**Async**

```python
result = await async_client.user_api.with_raw_response.delete_user(usersname)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>usersname</code> | <code>str</code> | The username that needs to be processed |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;None, [DeleteUserErrorBody](swagger_petstore_open_api_3_0/errors/delete_user_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteUserErrorBody](swagger_petstore_open_api_3_0/errors/delete_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_by_name(usersname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[User, GetUserByNameErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get user detail based on username.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_api.with_raw_response.get_user_by_name(usersname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type User
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUserByNameErrorBody
```

**Async**

```python
result = await async_client.user_api.with_raw_response.get_user_by_name(usersname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type User
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUserByNameErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>usersname</code> | <code>str</code> | The username that needs to be processed |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;[User](swagger_petstore_open_api_3_0/models/user.py), [GetUserByNameErrorBody](swagger_petstore_open_api_3_0/errors/get_user_by_name_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[User](swagger_petstore_open_api_3_0/models/user.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[GetUserByNameErrorBody](swagger_petstore_open_api_3_0/errors/get_user_by_name_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def login_user(*, username: str | None = None, password: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, LoginUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Log into the system.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_api.with_raw_response.login_user()
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LoginUserErrorBody
```

**Async**

```python
result = await async_client.user_api.with_raw_response.login_user()
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LoginUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str \| None</code> | The user name for login<br>**Default**: <code>None</code> |
| <code>password</code> | <code>str \| None</code> | The password for login in clear text<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;None, [LoginUserErrorBody](swagger_petstore_open_api_3_0/errors/login_user_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[LoginUserErrorBody](swagger_petstore_open_api_3_0/errors/login_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def logout_user(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Log user out of the system.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_api.with_raw_response.logout_user()
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.user_api.with_raw_response.logout_user()
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;None, [RawError](swagger_petstore_open_api_3_0/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_user(usersname: str, *, id: int | None = None, username: str | None = None, first_name: str | None = None, last_name: str | None = None, email: str | None = None, password: str | None = None, phone: str | None = None, user_status: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, UpdateUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This can only be done by the logged in user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_api.with_raw_response.update_user(usersname)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateUserErrorBody
```

**Async**

```python
result = await async_client.user_api.with_raw_response.update_user(usersname)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>usersname</code> | <code>str</code> | The username that needs to be processed |
| <code>id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>first_name</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>last_name</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>email</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>password</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>phone</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>user_status</code> | <code>int \| None</code> | User Status<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](swagger_petstore_open_api_3_0/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](swagger_petstore_open_api_3_0/core/results.py)&#91;None, [UpdateUserErrorBody](swagger_petstore_open_api_3_0/errors/update_user_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[UpdateUserErrorBody](swagger_petstore_open_api_3_0/errors/update_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |
| anything unmapped | <code>[RawError](swagger_petstore_open_api_3_0/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

