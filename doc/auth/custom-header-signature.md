
# Custom Header Signature



Documentation for accessing and setting credentials for api_key.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| api_key | `str` | - | `api_key` |



**Note:** Auth credentials can be set using `ApiKeyCredentials` object, passed in as named parameter `api_key_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from swaggerpetstoreopenapi30.http.auth.api_key import ApiKeyCredentials
from swaggerpetstoreopenapi30.swaggerpetstoreopenapi_30_client import Swaggerpetstoreopenapi30Client

client = Swaggerpetstoreopenapi30Client(
    api_key_credentials=ApiKeyCredentials(
        api_key='api_key'
    )
)
```


