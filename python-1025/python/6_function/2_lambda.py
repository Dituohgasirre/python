#!/usr/bin/env python3

def add(a, b):
    return a + b

def test(call, a, b):
    return call(a, b)

def main():
    a = add
    s = lambda a, b: a - b

    print("add: ", test(add, 5, 3))
    print("sub: ", test(lambda a, b: a + b, 5, 3))


if __name__ == "__main__":
    main()
