
# Order

*This model accepts additional fields of type Any.*

## Structure

`Order`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `pet_id` | `int` | Optional | - |
| `quantity` | `int` | Optional | - |
| `ship_date` | `datetime` | Optional | - |
| `status` | [`OrderStatus`](../../doc/models/order-status.md) | Optional | Order Status |
| `complete` | `bool` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from swaggerpetstoreopenapi30.models.order import Order
from swaggerpetstoreopenapi30.models.order_status import OrderStatus

order = Order(
    id=144,
    pet_id=184,
    quantity=100,
    ship_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    status=OrderStatus.PLACED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

