import decimal
import numbers
import math


def is_perfect_square(input: numbers.Number) -> bool:
    if isinstance(input, numbers.Number):
        if input < 0:
            return False
        root = math.sqrt(input)
        return int(root + 0.5) ** 2 == input
    raise TypeError


print(is_perfect_square(decimal.Decimal(64)))
print(is_perfect_square(65))
print(is_perfect_square(100))
print(is_perfect_square(1000))
print(is_perfect_square(-4))
print(is_perfect_square("hoge"))
