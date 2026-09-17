<!-- Generated file — do not edit; regenerated with the SDK. -->

# Store — operations

Accessor: `client.store` · Source: `swagger_petstore_open_api_3_0/apis/store.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.store.delete_order

- **Route**: `DELETE /store/order/{orderId}`
- **Server**: `default`
- **Signature**: `def delete_order(order_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`
- **Params**: `order_id` — path `orderId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteOrderErrorBody]`
- **Error**: `DeleteOrderErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteOrderErrorBody` | `swagger_petstore_open_api_3_0/errors/delete_order_error.py` |

### client.store.get_inventory

- **Route**: `GET /store/inventory`
- **Auth**: `api_key`
- **Server**: `default`
- **Signature**: `def get_inventory(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `dict[str, int]`
- **Returns (raw)**: `ApiResult[dict[str, int], RawError]`
- **Error**: `RawError` — **Case B**

### client.store.get_order_by_id

- **Route**: `GET /store/order/{orderId}`
- **Server**: `default`
- **Signature**: `def get_order_by_id(order_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`
- **Params**: `order_id` — path `orderId`
- **Returns (parsed)**: `Order`
- **Returns (raw)**: `ApiResult[Order, GetOrderByIdErrorBody]`
- **Error**: `GetOrderByIdErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, anything unmapped]

| Type | Source |
| --- | --- |
| `Order` | `swagger_petstore_open_api_3_0/models/order.py` |
| `GetOrderByIdErrorBody` | `swagger_petstore_open_api_3_0/errors/get_order_by_id_error.py` |

### client.store.place_order

- **Route**: `POST /store/order`
- **Server**: `default`
- **Signature**: `def place_order(*, id: int | None = None, pet_id: int | None = None, quantity: int | None = None, ship_date: RFC3339DateTime | None = None, status: OrderStatusOrStr | None = None, complete: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — form field · `pet_id` — form field `petId` · `quantity` — form field · `ship_date` — form field `shipDate` · `status` — form field · `complete` — form field
- **Returns (parsed)**: `Order`
- **Returns (raw)**: `ApiResult[Order, PlaceOrderErrorBody]`
- **Error**: `PlaceOrderErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 422, anything unmapped]

| Type | Source |
| --- | --- |
| `OrderStatusOrStr` | `swagger_petstore_open_api_3_0/models/enums/order_status.py` |
| `Order` | `swagger_petstore_open_api_3_0/models/order.py` |
| `PlaceOrderErrorBody` | `swagger_petstore_open_api_3_0/errors/place_order_error.py` |

