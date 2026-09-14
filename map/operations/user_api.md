<!-- Generated file — do not edit; regenerated with the SDK. -->

# UserApi — operations

Accessor: `client.user_api` · Source: `swagger_petstore_open_api_3_0/apis/user_api.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.user_api.create_user

- **Route**: `POST /user`
- **Server**: `default`
- **Signature**: `def create_user(*, id: int | None = None, username: str | None = None, first_name: str | None = None, last_name: str | None = None, email: str | None = None, password: str | None = None, phone: str | None = None, user_status: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — form field · `username` — form field · `first_name` — form field `firstName` · `last_name` — form field `lastName` · `email` — form field · `password` — form field · `phone` — form field · `user_status` — form field `userStatus`
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `swagger_petstore_open_api_3_0/models/user.py` |

### client.user_api.create_users_with_list_input

- **Route**: `POST /user/createWithList`
- **Server**: `default`
- **Signature**: `def create_users_with_list_input(*, body: list[User | UserDict] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `swagger_petstore_open_api_3_0/models/user.py` |
| `UserDict` | `swagger_petstore_open_api_3_0/models/user.py` |

### client.user_api.delete_user

- **Route**: `DELETE /user/{usersname}`
- **Server**: `default`
- **Signature**: `def delete_user(usersname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `usersname`
- **Params**: `usersname` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteUserErrorBody]`
- **Error**: `DeleteUserErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteUserErrorBody` | `swagger_petstore_open_api_3_0/errors/delete_user_error.py` |

### client.user_api.get_user_by_name

- **Route**: `GET /user/{usersname}`
- **Server**: `default`
- **Signature**: `def get_user_by_name(usersname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `usersname`
- **Params**: `usersname` — path
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, GetUserByNameErrorBody]`
- **Error**: `GetUserByNameErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `User` | `swagger_petstore_open_api_3_0/models/user.py` |
| `GetUserByNameErrorBody` | `swagger_petstore_open_api_3_0/errors/get_user_by_name_error.py` |

### client.user_api.login_user

- **Route**: `GET /user/login`
- **Server**: `default`
- **Signature**: `def login_user(*, username: str | None = None, password: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `username` — query · `password` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, LoginUserErrorBody]`
- **Error**: `LoginUserErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `LoginUserErrorBody` | `swagger_petstore_open_api_3_0/errors/login_user_error.py` |

### client.user_api.logout_user

- **Route**: `GET /user/logout`
- **Server**: `default`
- **Signature**: `def logout_user(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.user_api.update_user

- **Route**: `PUT /user/{usersname}`
- **Server**: `default`
- **Signature**: `def update_user(usersname: str, *, id: int | None = None, username: str | None = None, first_name: str | None = None, last_name: str | None = None, email: str | None = None, password: str | None = None, phone: str | None = None, user_status: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `usersname`
- **Params**: `usersname` — path · `id` — form field · `username` — form field · `first_name` — form field `firstName` · `last_name` — form field `lastName` · `email` — form field · `password` — form field · `phone` — form field · `user_status` — form field `userStatus`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UpdateUserErrorBody]`
- **Error**: `UpdateUserErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateUserErrorBody` | `swagger_petstore_open_api_3_0/errors/update_user_error.py` |

