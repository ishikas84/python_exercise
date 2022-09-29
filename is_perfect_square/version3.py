import numbers
from decimal import Decimal


def is_perfect_square(input: numbers.Number) -> bool:
    if isinstance(input, numbers.Number):
        if input < 0:
            return False
        input = Decimal(input)
        root = input.sqrt()
        return '.' not in str(root)
    raise TypeError


print(is_perfect_square(decimal.Decimal(64)))
print(is_perfect_square(65))
print(is_perfect_square(100))
print(is_perfect_square(1000))
print(is_perfect_square(-4))
# print(is_perfect_square("hoge"))
n = 838382848348234**2
m = 8383828483252752341748234**2
print(is_perfect_square(m))
print(is_perfect_square(m + 1))
