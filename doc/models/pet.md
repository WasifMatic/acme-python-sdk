
# Pet

*This model accepts additional fields of type Any.*

## Structure

`Pet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Required | - |
| `category` | [`Category`](../../doc/models/category.md) | Optional | - |
| `photo_urls` | `List[str]` | Required | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Optional | - |
| `status` | [`PetStatus`](../../doc/models/pet-status.md) | Optional | pet status in the store |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from swaggerpetstoreopenapi30.models.category import Category
from swaggerpetstoreopenapi30.models.pet import Pet
from swaggerpetstoreopenapi30.models.pet_status import PetStatus
from swaggerpetstoreopenapi30.models.tag import Tag

pet = Pet(
    name='name0',
    photo_urls=[
        'photoUrls5',
        'photoUrls6'
    ],
    id=72,
    category=Category(
        id=232,
        name='name2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    tags=[
        Tag(
            id=26,
            name='name0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    status=PetStatus.AVAILABLE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

