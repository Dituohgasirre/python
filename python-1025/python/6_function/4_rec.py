#!/usr/bin/env python3

import sys

count = 0

def test(n):
    global count
    if n == 0:
        return
    print("1 test: ", n, ", count = ", count)
    count += 1
    test(n - 1)
    count -= 1
    print("2 test: ", n, ", count = ", count)

def add(n):
    if n == 0:
        return 0
    return n + add(n - 1)

def main():
    #  test(10)
    sys.setrecursionlimit(1100000)
    print(add(10000))

if __name__ == "__main__":
    main()
