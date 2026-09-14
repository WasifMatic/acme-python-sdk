# Store

Access to Petstore orders

Find out more about our store: [https://swagger.io](https://swagger.io)

```python
store_api = client.store
```

## Class Name

`StoreApi`

## Methods

* [Get Inventory](../../doc/controllers/store.md#get-inventory)
* [Place Order](../../doc/controllers/store.md#place-order)
* [Get Order by Id](../../doc/controllers/store.md#get-order-by-id)
* [Delete Order](../../doc/controllers/store.md#delete-order)


# Get Inventory

Returns a map of status codes to quantities.

```python
def get_inventory(self)
```

## Authentication

This endpoint requires [api_key](../../doc/auth/custom-header-signature.md)

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Dict[str, int]`.

## Example Usage

```python
result = store_api.get_inventory()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | `ApiException` |


# Place Order

Place a new order in the store.

:information_source: **Note** This endpoint does not require authentication.

```python
def place_order(self,
               id=None,
               pet_id=None,
               quantity=None,
               ship_date=None,
               status=None,
               complete=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Form, Optional | - |
| `pet_id` | `int` | Form, Optional | - |
| `quantity` | `int` | Form, Optional | - |
| `ship_date` | `datetime` | Form, Optional | - |
| `status` | [`OrderStatus`](../../doc/models/order-status.md) | Form, Optional | Order Status |
| `complete` | `bool` | Form, Optional | - |

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Order`](../../doc/models/order.md).

## Example Usage

```python
id = 10

pet_id = 198772

quantity = 7

result = store_api.place_order(
    id=id,
    pet_id=pet_id,
    quantity=quantity
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid input | `ApiException` |
| 422 | Validation exception | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Get Order by Id

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_order_by_id(self,
                   order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `int` | Template, Required | ID of order that needs to be fetched |

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Order`](../../doc/models/order.md).

## Example Usage

```python
order_id = 62

result = store_api.get_order_by_id(order_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `ApiException` |
| 404 | Order not found | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Delete Order

For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_order(self,
                order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `int` | Template, Required | ID of the order that needs to be deleted |

## Response Type

**200**: order deleted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
order_id = 62

result = store_api.delete_order(order_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `ApiException` |
| 404 | Order not found | `ApiException` |
| Default | Unexpected error | `ApiException` |

