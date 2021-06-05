#!/usr/bin/env python3

class Test:
    def __init__(self):
        pass

    def get(self, name):
        if name in c.__dict__:
            return c.__dict__[name]
        return None

    def run(self):
        print("Test Run")

    def __str__(self):
        return ""

if __name__ == "__main__":
    c = Test()
    c.age = 34
    setattr(c, 'age', 66)       # c.age = 66
    delattr(c, 'age')           # del c.age
    #  if hasattr(c, 'age'):
    print(getattr(c, 'age', 99))
    #  print(c.get('age'))
    print(c)

    v = getattr(c, 'run')
    v()
