#!/usr/bin/env python3

class Mymap:
    def __init__(self, op, *args):
        self.data = iter(self.run(op, *args))

    def run(self, op, *args):
        m = len(args[0])
        for i in range(1, len(args)):
            l = len(args[i])
            if m > l:
                m = l

        for i in range(m):
            s = []
            for a in args:
                s.append(a[i])
            yield op(*s)

    def __str__(self):
        return "<Mymap at " + hex(id(self)) + ">"

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)

class Test:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]
        self.len = len(self.data)

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num == self.len:
            raise StopIteration

        ret = self.data[self.num]
        self.num += 1
        return ret


def main():
    s = Mymap(lambda a, b: a + b, [1, 2, 3], [4, 5, 6])
    print(s)
    for i in s:
        print(i)

    a = Test()

    for i in a:
        print(i)

    for i in a:
        print(i)


if __name__ == "__main__":
    main()
