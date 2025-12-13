from decorators.clamp import clamp_result
from decorators.validate import validate_numeric
from decorators.convert import float_to_int


@clamp_result(0, 100)
@validate_numeric
@float_to_int
def compute(x, y):
    return x * y - 30


@clamp_result(-10, 10)
@float_to_int
def difference(a, b):
    return a - b
