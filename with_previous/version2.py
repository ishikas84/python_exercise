def with_previous(sequence):
    prev = None
    for elm in sequence:
        yield (elm, prev)
        prev = elm


print(list(with_previous("hello")))
print(list(with_previous([1, 2, 3])))
print(list(with_previous(n**2 for n in [1, 2, 3])))
print(next(with_previous([1, 2, 3])))
