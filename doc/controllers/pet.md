# Pet

Everything about your Pets

Find out more: [https://swagger.io](https://swagger.io)

```python
pet_api = client.pet
```

## Class Name

`PetApi`

## Methods

* [Update Pet](../../doc/controllers/pet.md#update-pet)
* [Add Pet](../../doc/controllers/pet.md#add-pet)
* [Find Pets by Status](../../doc/controllers/pet.md#find-pets-by-status)
* [Find Pets by Tags](../../doc/controllers/pet.md#find-pets-by-tags)
* [Get Pet by Id](../../doc/controllers/pet.md#get-pet-by-id)
* [Update Pet with Form](../../doc/controllers/pet.md#update-pet-with-form)
* [Delete Pet](../../doc/controllers/pet.md#delete-pet)
* [Upload File](../../doc/controllers/pet.md#upload-file)


# Update Pet

Update an existing pet by Id.

```python
def update_pet(self,
              name,
              photo_urls,
              id=None,
              category=None,
              tags=None,
              status=None)
```

## Authentication

This endpoint requires [petstore_auth](../../doc/auth/oauth-2-implicit-grant.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Form, Required | - |
| `photo_urls` | `List[str]` | Form, Required | - |
| `id` | `int` | Form, Optional | - |
| `category` | [`Category`](../../doc/models/category.md) | Form, Optional | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Form, Optional | - |
| `status` | [`PetStatus`](../../doc/models/pet-status.md) | Form, Optional | pet status in the store |

## Requires scope

### petstore_auth

`read:pets`, `write:pets`

## Response Type

**200**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Pet`](../../doc/models/pet.md).

## Example Usage

```python
name = 'doggie'

photo_urls = [
    'photoUrls5',
    'photoUrls6',
    'photoUrls7'
]

id = 10

tags = [
    Tag()
]

result = pet_api.update_pet(
    name,
    photo_urls,
    id=id,
    tags=tags
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `ApiException` |
| 404 | Pet not found | `ApiException` |
| 422 | Validation exception | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Add Pet

Add a new pet to the store.

```python
def add_pet(self,
           name,
           photo_urls,
           id=None,
           category=None,
           tags=None,
           status=None)
```

## Authentication

This endpoint requires [petstore_auth](../../doc/auth/oauth-2-implicit-grant.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Form, Required | - |
| `photo_urls` | `List[str]` | Form, Required | - |
| `id` | `int` | Form, Optional | - |
| `category` | [`Category`](../../doc/models/category.md) | Form, Optional | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Form, Optional | - |
| `status` | [`PetStatus`](../../doc/models/pet-status.md) | Form, Optional | pet status in the store |

## Requires scope

### petstore_auth

`read:pets`, `write:pets`

## Response Type

**200**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Pet`](../../doc/models/pet.md).

## Example Usage

```python
name = 'doggie'

photo_urls = [
    'photoUrls5',
    'photoUrls6',
    'photoUrls7'
]

id = 10

tags = [
    Tag()
]

result = pet_api.add_pet(
    name,
    photo_urls,
    id=id,
    tags=tags
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


# Find Pets by Status

Multiple status values can be provided with comma separated strings.

```python
def find_pets_by_status(self,
                       status=None)
```

## Authentication

This endpoint requires [petstore_auth](../../doc/auth/oauth-2-implicit-grant.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`PetStatus`](../../doc/models/pet-status.md) | Query, Optional | Status values that need to be considered for filter |

## Requires scope

### petstore_auth

`read:pets`, `write:pets`

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Pet]`](../../doc/models/pet.md).

## Example Usage

```python
result = pet_api.find_pets_by_status()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid status value | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Find Pets by Tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

```python
def find_pets_by_tags(self,
                     tags=None)
```

## Authentication

This endpoint requires [petstore_auth](../../doc/auth/oauth-2-implicit-grant.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tags` | `List[str]` | Query, Optional | Tags to filter by |

## Requires scope

### petstore_auth

`read:pets`, `write:pets`

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Pet]`](../../doc/models/pet.md).

## Example Usage

```python
result = pet_api.find_pets_by_tags()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid tag value | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Get Pet by Id

Returns a single pet.

```python
def get_pet_by_id(self,
                 pet_id)
```

## Authentication

This endpoint requires [api_key](../../doc/auth/custom-header-signature.md) **OR** [petstore_auth](../../doc/auth/oauth-2-implicit-grant.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_id` | `int` | Template, Required | ID of pet to return |

## Requires scope

### petstore_auth

`read:pets`, `write:pets`

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Pet`](../../doc/models/pet.md).

## Example Usage

```python
pet_id = 10

result = pet_api.get_pet_by_id(pet_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `ApiException` |
| 404 | Pet not found | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Update Pet with Form

Updates a pet resource based on the form data.

```python
def update_pet_with_form(self,
                        pet_id,
                        name=None,
                        status=None)
```

## Authentication

This endpoint requires [petstore_auth](../../doc/auth/oauth-2-implicit-grant.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_id` | `int` | Template, Required | ID of pet that needs to be updated |
| `name` | `str` | Query, Optional | Name of pet that needs to be updated |
| `status` | `str` | Query, Optional | Status of pet that needs to be updated |

## Requires scope

### petstore_auth

`read:pets`, `write:pets`

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Pet`](../../doc/models/pet.md).

## Example Usage

```python
pet_id = 10

result = pet_api.update_pet_with_form(pet_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid input | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Delete Pet

Delete a pet.

```python
def delete_pet(self,
              pet_id,
              api_key=None)
```

## Authentication

This endpoint requires [petstore_auth](../../doc/auth/oauth-2-implicit-grant.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_id` | `int` | Template, Required | Pet id to delete |
| `api_key` | `str` | Header, Optional | - |

## Requires scope

### petstore_auth

`read:pets`, `write:pets`

## Response Type

**200**: Pet deleted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
pet_id = 10

result = pet_api.delete_pet(pet_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid pet value | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Upload File

Upload image of the pet.

```python
def upload_file(self,
               pet_id,
               additional_metadata=None,
               body=None)
```

## Authentication

This endpoint requires [petstore_auth](../../doc/auth/oauth-2-implicit-grant.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_id` | `int` | Template, Required | ID of pet to update |
| `additional_metadata` | `str` | Query, Optional | Additional Metadata |
| `body` | `typing.BinaryIO` | Form, Optional | - |

## Requires scope

### petstore_auth

`read:pets`, `write:pets`

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ApiResponse`](../../doc/models/api-response.md).

## Example Usage

```python
pet_id = 10

result = pet_api.upload_file(pet_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | No file uploaded | `ApiException` |
| 404 | Pet not found | `ApiException` |
| Default | Unexpected error | `ApiException` |

