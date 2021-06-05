#!/usr/bin/env python3

class Test:
    __slots__ = ('name', 'age', 'en')
    def __init__(self):
        self.cn = 456

    def __str__(self):
        return ""

if __name__ == "__main__":
    c = Test()
    c.name = 34
    c.age = 34
    c.en = 34
    del c.en
    c.en = 78
    c.www = 345
    print(c)
