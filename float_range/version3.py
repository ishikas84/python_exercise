class float_range:
    def __init__(self, start, end=None, step=1):
        if end is None:
            self.start = 0.0
            self.end = start
        else:
            self.start = start
            self.end = end
        self.step = step

    def __repr__(self):
        return f"float_range{self.start, self.end, self.step}"

    def __len__(self):
        return len(list(self.__iter__()))

    def __iter__(self):
        if self.step >= 0:
            counter = self.start
            while counter < self.end:
                yield counter
                counter += self.step
        else:
            counter = self.start
            while counter > self.end:
                yield counter
                counter += self.step

    def __getitem__(self, key):
        return list(self.__iter__())[key]

    def __eq__(self, other):
        if isinstance(other, range) or isinstance(other, float_range):
            if len(list(other)) == len(list(self.__iter__())):
                for o, item in zip(other, self.__iter__()):
                    if o != item:
                        return False
                return True
        return False


if __name__ == '__main__':
    a = float_range(0.5, 2.5, 0.5)
    print(list(a))
    print(list(float_range(3.5, 0, -1)))
    print(len(list(float_range(3.5, 0, -1))))
    print(len(a))
    for n in float_range(0.0, 3.0):
        print(n)
    for n in float_range(3.0):
        print(n)

    my_range = float_range(0.5, 7, 0.75)
    print(my_range[1])
    print(my_range[-1])
    a = float_range(0.5, 2.5, 0.5)
    b = float_range(0.5, 2.5, 0.5)
    c = float_range(0.5, 3.0, 0.5)
    print(a == b)
    print(a == c)
    print(float_range(5) == range(0, 5))
    print(float_range(4) == range(5))
    print(float_range(4) == 3)
    print(type(float_range(5)), type(range(0, 5)))