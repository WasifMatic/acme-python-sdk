# User

Operations about user

```python
user_api = client.user
```

## Class Name

`UserApi`

## Methods

* [Create User](../../doc/controllers/user.md#create-user)
* [Create Users with List Input](../../doc/controllers/user.md#create-users-with-list-input)
* [Login User](../../doc/controllers/user.md#login-user)
* [Logout User](../../doc/controllers/user.md#logout-user)
* [Get User by Name](../../doc/controllers/user.md#get-user-by-name)
* [Update User](../../doc/controllers/user.md#update-user)
* [Delete User](../../doc/controllers/user.md#delete-user)


# Create User

This can only be done by the logged in user.

:information_source: **Note** This endpoint does not require authentication.

```python
def create_user(self,
               id=None,
               username=None,
               first_name=None,
               last_name=None,
               email=None,
               password=None,
               phone=None,
               user_status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Form, Optional | - |
| `username` | `str` | Form, Optional | - |
| `first_name` | `str` | Form, Optional | - |
| `last_name` | `str` | Form, Optional | - |
| `email` | `str` | Form, Optional | - |
| `password` | `str` | Form, Optional | - |
| `phone` | `str` | Form, Optional | - |
| `user_status` | `int` | Form, Optional | User Status |

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`User`](../../doc/models/user.md).

## Example Usage

```python
id = 10

username = 'theUser'

first_name = 'John'

last_name = 'James'

email = 'john@email.com'

password = '12345'

phone = '12345'

user_status = 1

result = user_api.create_user(
    id=id,
    username=username,
    first_name=first_name,
    last_name=last_name,
    email=email,
    password=password,
    phone=phone,
    user_status=user_status
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | `ApiException` |


# Create Users with List Input

Creates list of users with given input array.

:information_source: **Note** This endpoint does not require authentication.

```python
def create_users_with_list_input(self,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List[User]`](../../doc/models/user.md) | Body, Optional | - |

## Response Type

**200**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`User`](../../doc/models/user.md).

## Example Usage

```python
body = [
    User()
]

result = user_api.create_users_with_list_input(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | `ApiException` |


# Login User

Log into the system.

:information_source: **Note** This endpoint does not require authentication.

```python
def login_user(self,
              username=None,
              password=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Query, Optional | The user name for login |
| `password` | `str` | Query, Optional | The password for login in clear text |

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = user_api.login_user()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username/password supplied | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Logout User

Log user out of the system.

:information_source: **Note** This endpoint does not require authentication.

```python
def logout_user(self)
```

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
result = user_api.logout_user()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | `ApiException` |


# Get User by Name

Get user detail based on username.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_user_by_name(self,
                    usersname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `usersname` | `str` | Template, Required | The username that needs to be processed |

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`User`](../../doc/models/user.md).

## Example Usage

```python
usersname = 'usersname0'

result = user_api.get_user_by_name(usersname)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username supplied | `ApiException` |
| 404 | User not found | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Update User

This can only be done by the logged in user.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_user(self,
               usersname,
               id=None,
               username=None,
               first_name=None,
               last_name=None,
               email=None,
               password=None,
               phone=None,
               user_status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `usersname` | `str` | Template, Required | The username that needs to be processed |
| `id` | `int` | Form, Optional | - |
| `username` | `str` | Form, Optional | - |
| `first_name` | `str` | Form, Optional | - |
| `last_name` | `str` | Form, Optional | - |
| `email` | `str` | Form, Optional | - |
| `password` | `str` | Form, Optional | - |
| `phone` | `str` | Form, Optional | - |
| `user_status` | `int` | Form, Optional | User Status |

## Response Type

**200**: successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
usersname = 'usersname0'

id = 10

username = 'theUser'

first_name = 'John'

last_name = 'James'

email = 'john@email.com'

password = '12345'

phone = '12345'

user_status = 1

result = user_api.update_user(
    usersname,
    id=id,
    username=username,
    first_name=first_name,
    last_name=last_name,
    email=email,
    password=password,
    phone=phone,
    user_status=user_status
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | `ApiException` |
| 404 | user not found | `ApiException` |
| Default | Unexpected error | `ApiException` |


# Delete User

This can only be done by the logged in user.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_user(self,
               usersname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `usersname` | `str` | Template, Required | The username that needs to be processed |

## Response Type

**200**: User deleted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
usersname = 'usersname0'

result = user_api.delete_user(usersname)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username supplied | `ApiException` |
| 404 | User not found | `ApiException` |
| Default | Unexpected error | `ApiException` |

