
# ProxySettings

Represents the proxy server configurations for API calls.

## Properties

| Name | Type | Tag | Description |
|  --- | --- | --- | --- |
| address | `str` | required | The proxy server URL. |
| port | `int` | optional | The port to connect to the proxy server. |
| username | `str` | optional | Username for proxy authentication. |
| password | `str` | optional | Password for proxy authentication. |

## Usage Example

```python
from swaggerpetstoreopenapi30.swaggerpetstoreopenapi_30_client import Swaggerpetstoreopenapi30Client
from swaggerpetstoreopenapi30.http.proxy_settings import ProxySettings

client = Swaggerpetstoreopenapi30Client(
    proxy_settings=ProxySettings(
        address='http://localhost',
        port=8888,
        username='user',
        password='pass'
     )
)
```

