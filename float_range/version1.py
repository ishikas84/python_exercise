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
    