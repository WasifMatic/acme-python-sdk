
# User

*This model accepts additional fields of type Any.*

## Structure

`User`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `username` | `str` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `password` | `str` | Optional | - |
| `phone` | `str` | Optional | - |
| `user_status` | `int` | Optional | User Status |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from swaggerpetstoreopenapi30.models.user import User

user = User(
    id=76,
    username='username0',
    first_name='firstName4',
    last_name='lastName4',
    email='email6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

