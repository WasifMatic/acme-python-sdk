<!-- Generated file — do not edit; regenerated with the SDK. -->

# PetApi — operations

Accessor: `client.pet_api` · Source: `swagger_petstore_open_api_3_0/apis/pet_api.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.pet_api.add_pet

- **Route**: `POST /pet`
- **Auth**: `petstore_auth`
- **Server**: `default`
- **Signature**: `def add_pet(name: str, photo_urls: list[str], *, id: int | None = None, category: Category | CategoryDict | None = None, tags: list[TagModel | TagModelDict] | None = None, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`, `photo_urls`
- **Params**: `name` — form field · `photo_urls` — form field `photoUrls` · `id` — form field · `category` — form field · `tags` — form field · `status` — form field
- **Returns (parsed)**: `Pet`
- **Returns (raw)**: `ApiResult[Pet, AddPetErrorBody]`
- **Error**: `AddPetErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 422, anything unmapped]

| Type | Source |
| --- | --- |
| `Category` | `swagger_petstore_open_api_3_0/models/category.py` |
| `CategoryDict` | `swagger_petstore_open_api_3_0/models/category.py` |
| `TagModel` | `swagger_petstore_open_api_3_0/models/tag_model.py` |
| `TagModelDict` | `swagger_petstore_open_api_3_0/models/tag_model.py` |
| `PetStatusOrStr` | `swagger_petstore_open_api_3_0/models/enums/pet_status.py` |
| `Pet` | `swagger_petstore_open_api_3_0/models/pet.py` |
| `AddPetErrorBody` | `swagger_petstore_open_api_3_0/errors/add_pet_error.py` |

### client.pet_api.delete_pet

- **Route**: `DELETE /pet/{petId}`
- **Auth**: `petstore_auth`
- **Server**: `default`
- **Signature**: `def delete_pet(pet_id: int, *, api_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `pet_id`
- **Params**: `pet_id` — path `petId` · `api_key` — header
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeletePetErrorBody]`
- **Error**: `DeletePetErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `DeletePetErrorBody` | `swagger_petstore_open_api_3_0/errors/delete_pet_error.py` |

### client.pet_api.find_pets_by_status

- **Route**: `GET /pet/findByStatus`
- **Auth**: `petstore_auth`
- **Server**: `default`
- **Signature**: `def find_pets_by_status(*, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query
- **Returns (parsed)**: `list[Pet]`
- **Returns (raw)**: `ApiResult[list[Pet], FindPetsByStatusErrorBody]`
- **Error**: `FindPetsByStatusErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `PetStatusOrStr` | `swagger_petstore_open_api_3_0/models/enums/pet_status.py` |
| `Pet` | `swagger_petstore_open_api_3_0/models/pet.py` |
| `FindPetsByStatusErrorBody` | `swagger_petstore_open_api_3_0/errors/find_pets_by_status_error.py` |

### client.pet_api.find_pets_by_tags

- **Route**: `GET /pet/findByTags`
- **Auth**: `petstore_auth`
- **Server**: `default`
- **Signature**: `def find_pets_by_tags(*, tags: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `tags` — query
- **Returns (parsed)**: `list[Pet]`
- **Returns (raw)**: `ApiResult[list[Pet], FindPetsByTagsErrorBody]`
- **Error**: `FindPetsByTagsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `Pet` | `swagger_petstore_open_api_3_0/models/pet.py` |
| `FindPetsByTagsErrorBody` | `swagger_petstore_open_api_3_0/errors/find_pets_by_tags_error.py` |

### client.pet_api.get_pet_by_id

- **Route**: `GET /pet/{petId}`
- **Auth**: `api_key` OR `petstore_auth`
- **Server**: `default`
- **Signature**: `def get_pet_by_id(pet_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `pet_id`
- **Params**: `pet_id` — path `petId`
- **Returns (parsed)**: `Pet`
- **Returns (raw)**: `ApiResult[Pet, GetPetByIdErrorBody]`
- **Error**: `GetPetByIdErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `Pet` | `swagger_petstore_open_api_3_0/models/pet.py` |
| `GetPetByIdErrorBody` | `swagger_petstore_open_api_3_0/errors/get_pet_by_id_error.py` |

### client.pet_api.update_pet

- **Route**: `PUT /pet`
- **Auth**: `petstore_auth`
- **Server**: `default`
- **Signature**: `def update_pet(name: str, photo_urls: list[str], *, id: int | None = None, category: Category | CategoryDict | None = None, tags: list[TagModel | TagModelDict] | None = None, status: PetStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`, `photo_urls`
- **Params**: `name` — form field · `photo_urls` — form field `photoUrls` · `id` — form field · `category` — form field · `tags` — form field · `status` — form field
- **Returns (parsed)**: `Pet`
- **Returns (raw)**: `ApiResult[Pet, UpdatePetErrorBody]`
- **Error**: `UpdatePetErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, 422, anything unmapped]

| Type | Source |
| --- | --- |
| `Category` | `swagger_petstore_open_api_3_0/models/category.py` |
| `CategoryDict` | `swagger_petstore_open_api_3_0/models/category.py` |
| `TagModel` | `swagger_petstore_open_api_3_0/models/tag_model.py` |
| `TagModelDict` | `swagger_petstore_open_api_3_0/models/tag_model.py` |
| `PetStatusOrStr` | `swagger_petstore_open_api_3_0/models/enums/pet_status.py` |
| `Pet` | `swagger_petstore_open_api_3_0/models/pet.py` |
| `UpdatePetErrorBody` | `swagger_petstore_open_api_3_0/errors/update_pet_error.py` |

### client.pet_api.update_pet_with_form

- **Route**: `POST /pet/{petId}`
- **Auth**: `petstore_auth`
- **Server**: `default`
- **Signature**: `def update_pet_with_form(pet_id: int, *, name: str | None = None, status: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `pet_id`
- **Params**: `pet_id` — path `petId` · `name` — query · `status` — query
- **Returns (parsed)**: `Pet`
- **Returns (raw)**: `ApiResult[Pet, UpdatePetWithFormErrorBody]`
- **Error**: `UpdatePetWithFormErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `Pet` | `swagger_petstore_open_api_3_0/models/pet.py` |
| `UpdatePetWithFormErrorBody` | `swagger_petstore_open_api_3_0/errors/update_pet_with_form_error.py` |

### client.pet_api.upload_file

- **Route**: `POST /pet/{petId}/uploadImage`
- **Auth**: `petstore_auth`
- **Server**: `default`
- **Signature**: `def upload_file(pet_id: int, *, additional_metadata: str | None = None, body: FileInput | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `pet_id`
- **Params**: `pet_id` — path `petId` · `additional_metadata` — query `additionalMetadata` · `body` — binary body
- **Returns (parsed)**: `ApiResponse`
- **Returns (raw)**: `ApiResult[ApiResponse, UploadFileErrorBody]`
- **Error**: `UploadFileErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `ApiResponse` | `swagger_petstore_open_api_3_0/models/api_response.py` |
| `UploadFileErrorBody` | `swagger_petstore_open_api_3_0/errors/upload_file_error.py` |

