#!/usr/bin/env python3

class Test:
    def __init__(self):
        pass

    def __call__(self):
        with open("/tmp/test.file") as f:
            #  print(f.read())
            for num, line in enumerate(f, 1):
                print(num, ": ", line, sep="", end='')


if __name__ == "__main__":
    Test()()
