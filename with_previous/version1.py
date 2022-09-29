def with_previous(sequence: list):
    prev = None
    counter = 0
    while counter < len(sequence):
        yield (sequence[counter], prev)
        prev = sequence[counter]
        counter += 1


print(list(with_previous("hello")))
print(list(with_previous([1, 2, 3])))
