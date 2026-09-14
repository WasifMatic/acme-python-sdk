
# Api Response

*This model accepts additional fields of type Any.*

## Structure

`ApiResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `int` | Optional | - |
| `mtype` | `str` | Optional | - |
| `message` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from swaggerpetstoreopenapi30.models.api_response import ApiResponse

api_response = ApiResponse(
    code=102,
    mtype='type8',
    message='message8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

