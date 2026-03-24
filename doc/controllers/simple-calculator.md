# Simple Calculator

```python
simple_calculator_controller = client.simple_calculator
```

## Class Name

`SimpleCalculatorController`


# Calculate

Calculates the expression using the specified operation.

```python
def calculate(self,
             operation,
             x,
             y)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | [`OperationTypeEnum`](../../doc/models/operation-type-enum.md) | Template, Required | The operator to apply on the variables |
| `x` | `float` | Query, Required | The LHS value |
| `y` | `float` | Query, Required | The RHS value |

## Response Type

`float`

## Example Usage

```python
operation = OperationTypeEnum.SUM

x = 222.14

y = 165.14

result = simple_calculator_controller.calculate(
    operation,
    x,
    y
)
print(result)
```

