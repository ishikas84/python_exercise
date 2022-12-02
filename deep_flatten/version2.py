from collections import deque


def deep_flatten(inputs):
    output = []
    for elements in inputs:
        if hasattr(elements, '__iter__'):
            a = deep_flatten(elements)
            output += a
        else:
            output.append(elements)
    return output


print(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]))
print(deep_flatten([[1, [2, 3]], 4, 5]))
print(sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)})))
print(deep_flatten([(1, 2), deque([3])]))
print(deep_flatten(iter([n]) for n in [1, 2, 3]))