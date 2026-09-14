
# Getting Started with APIMATIC Calculator

## Introduction

Simple calculator API hosted on APIMATIC

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install cliV1==0.1.5
```

You can also view the package at:
https://pypi.python.org/pypi/cliV1/0.1.5

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
from apimaticcalculator.apimaticcalculator_client import ApimaticcalculatorClient
from apimaticcalculator.configuration import Environment

client = ApimaticcalculatorClient(
    environment=Environment.PRODUCTION
)
```

### Environment-Based Client Initialization

```python
from apimaticcalculator.apimaticcalculator_client import ApimaticcalculatorClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = ApimaticcalculatorClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/environment-based-client-initialization.md) section for details.

## List of APIs

* [Simple Calculator](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/controllers/simple-calculator.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/proxy-settings.md)
* [Environment-Based Client Initialization](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/environment-based-client-initialization.md)

### HTTP

* [HttpResponse](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/http-response.md)
* [HttpRequest](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/http-request.md)

### Utilities

* [ApiHelper](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/WasifMatic/acme-python-sdk/tree/0.1.5/doc/unix-date-time.md)

