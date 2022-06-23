class OrderedSet:
    def __init__(self, iterable):
        self.ordered_set = dict.fromkeys(iterable, None)

    def __contains__(self, item):
        return item in self.ordered_set

    def __iter__(self):
        yield from self.ordered_set

    def __len__(self):
        return len(self.ordered_set)

    def add(self, word):
        if word not in self.ordered_set:
            self.ordered_set[word] = None

    def discard(self, word):
        if word in self.ordered_set:
            del self.ordered_set[word]

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return (
                tuple(self) == tuple(other)
            )
        elif isinstance(other, set):
            return (
                all(x in other for x in self)
            )
        return NotImplemented

    def __getitem__(self, index):
        return list(self.ordered_set.keys())[index]
