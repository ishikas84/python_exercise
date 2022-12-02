
def deep_flatten(inputs):
    output = []
    for elements in inputs:
        if isinstance(elements, list) or isinstance(elements, tuple):
            a = deep_flatten(elements)
            output += a
        else:
            output.append(elements)
    return output


print(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]))
print(deep_flatten([[1, [2, 3]], 4, 5]))
