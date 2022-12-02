from collections import deque, abc


def deep_flatten(inputs):

    for el in inputs:
        if isinstance(el, abc.Iterable) and not isinstance(el, (str, bytes)):
            yield from deep_flatten(el)
        else:
            yield el


squares = (n**2 for n in [1, 2, 3])

print(list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']])))
print(list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])))
print(list(deep_flatten([[1, [2, 3]], 4, 5])))
print(sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)})))
print(list(deep_flatten([(1, 2), deque([3])])))
print(list(deep_flatten(iter([n]) for n in [1, 2, 3])))
print(next(deep_flatten(squares)))
print(next(squares))
