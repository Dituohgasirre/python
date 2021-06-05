#!/usr/bin/env python3

class TestInt:
    def __init__(self, num=0):
        if type(num) == str:
            self.num = 0
            for c in num:
                self.num = self.num * 10 + ord(c) - 48
        else:
            self.num = num

    def __add__(self, num):         #obj + 30
        return self.num + num

    def __iadd__(self, num):        #obj += 10
        self.num += num
        return self

    def __radd__(self, num):        #30 + obj
        return num + self.num

    def __sub__(self, num):
        return self.num - num

    def __str__(self):
        return "%d" % self.num


if __name__ == "__main__":
    c = TestInt("600")
    print(c + 30)
    print(30 + c)
    print(c - 30)
    c += 30
    print(c, type(c))
