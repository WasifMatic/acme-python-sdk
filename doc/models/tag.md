
# Tag

*This model accepts additional fields of type Any.*

## Structure

`Tag`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from swaggerpetstoreopenapi30.models.tag import Tag

tag = Tag(
    id=168,
    name='name6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

