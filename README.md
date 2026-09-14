
# Getting Started with Swagger Petstore - OpenAPI 3.0

## Introduction

This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about
Swagger at [https://swagger.io](https://swagger.io). In the third iteration of the pet store, we've switched to the design first approach!
You can now help us improve the API whether it's by making changes to the definition itself or to the code.
That way, with time, we can improve the API in general, and expose some of the new features in OAS3.

Some useful links:

- [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
- [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)

Find out more about Swagger: [https://swagger.io](https://swagger.io)

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install cliV1==0.1.4
```

You can also view the package at:
https://pypi.python.org/pypi/cliV1/0.1.4

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | [`Environment`](README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT", "GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](doc/logging-configuration.md) | The SDK logging configuration for API calls |
| petstore_auth_credentials | [`PetstoreAuthCredentials`](doc/auth/oauth-2-implicit-grant.md) | The credential object for OAuth 2 Implicit Grant |
| api_key_credentials | [`ApiKeyCredentials`](doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

### Code-Based Client Initialization

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

### Environment-Based Client Initialization

```python
from swaggerpetstoreopenapi30.swaggerpetstoreopenapi_30_client import Swaggerpetstoreopenapi30Client

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = Swaggerpetstoreopenapi30Client.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| PRODUCTION | **Default** |

## Authorization

This API uses the following authentication schemes.

* [`petstore_auth (OAuth 2 Implicit Grant)`](doc/auth/oauth-2-implicit-grant.md)
* [`api_key (Custom Header Signature)`](doc/auth/custom-header-signature.md)

## List of APIs

* [Pet](doc/controllers/pet.md)
* [Store](doc/controllers/store.md)
* [User](doc/controllers/user.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](doc/proxy-settings.md)
* [Environment-Based Client Initialization](doc/environment-based-client-initialization.md)
* [AbstractLogger](doc/abstract-logger.md)
* [LoggingConfiguration](doc/logging-configuration.md)
* [RequestLoggingConfiguration](doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

### Utilities

* [ApiResponse](doc/api-response.md)
* [ApiHelper](doc/api-helper.md)
* [HttpDateTime](doc/http-date-time.md)
* [RFC3339DateTime](doc/rfc3339-date-time.md)
* [UnixDateTime](doc/unix-date-time.md)

