from collections import deque
from itertools import chain, islice, repeat


def window(iterable, n, *, fillvalue=None):
    if n == 0:
        return
    iterator = iter(iterable)
    first_n_items = islice(chain(iterator, repeat(fillvalue)), n)
    current = deque(first_n_items, maxlen=n)
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)