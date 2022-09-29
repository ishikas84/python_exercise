def with_previous(sequence, *, fillvalue=None):
    prev = fillvalue
    for elm in sequence:
        yield (elm, prev)
        prev = elm


print(list(with_previous([1, 2, 3], fillvalue=0)))
