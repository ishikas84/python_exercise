from collections import deque


def window(iterable, n):
    """Yield tuples including iterable item and the next n-1 items."""
    current = deque(maxlen=n)
    for item in iterable:
        current.append(item)
        if n and len(current) == n:
            yield tuple(current)



# numbers = [1, 2, 3, 4, 5, 6]
# squares = (n**2 for n in numbers)
# print(list(window(numbers, 2)))
# print(list(window(numbers, 3)))
# print(list(window(squares, 4)))
# print(list(window(numbers, 0)))

inputs = (n**2 for n in [1, 2, 3, 4, 5])
iterable = window(inputs, 2)
# print(iter(iterable), iter(iterable))
print(next(iterable))
print(next(iterable), (1, 4))
print(next(inputs), 9)
print(list(iterable), [(4, 16), (16, 25)])