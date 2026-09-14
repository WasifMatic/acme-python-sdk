
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | [`Environment`](../README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT", "GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](../doc/logging-configuration.md) | The SDK logging configuration for API calls |
| petstore_auth_credentials | [`PetstoreAuthCredentials`](auth/oauth-2-implicit-grant.md) | The credential object for OAuth 2 Implicit Grant |
| api_key_credentials | [`ApiKeyCredentials`](auth/custom-header-signature.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
import logging

from swaggerpetstoreopenapi30.configuration import Environment
from swaggerpetstoreopenapi30.http.auth.api_key import ApiKeyCredentials
from swaggerpetstoreopenapi30.http.auth.petstore_auth import PetstoreAuthCredentials
from swaggerpetstoreopenapi30.logging.configuration.api_logging_configuration import LoggingConfiguration
from swaggerpetstoreopenapi30.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from swaggerpetstoreopenapi30.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from swaggerpetstoreopenapi30.models.oauth_scope_petstore_auth import OauthScopePetstoreAuth
from swaggerpetstoreopenapi30.swaggerpetstoreopenapi_30_client import Swaggerpetstoreopenapi30Client

client = Swaggerpetstoreopenapi30Client(
    petstore_auth_credentials=PetstoreAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_redirect_uri='OAuthRedirectUri',
        oauth_scopes=[
            OauthScopePetstoreAuth.WRITEPETS,
            OauthScopePetstoreAuth.READPETS
        ]
    ),
    api_key_credentials=ApiKeyCredentials(
        api_key='api_key'
    ),
    environment=Environment.PRODUCTION,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Environment-Based Client Initialization

```python
from swaggerpetstoreopenapi30.swaggerpetstoreopenapi_30_client import Swaggerpetstoreopenapi30Client

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = Swaggerpetstoreopenapi30Client.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## Swagger Petstore - OpenAPI 3.0 Client

The gateway for the SDK. This class acts as a factory for the Apis and also holds the configuration of the SDK.

## Apis

| Name | Description |
|  --- | --- |
| pet | Gets PetApi |
| store | Gets StoreApi |
| user | Gets UserApi |

