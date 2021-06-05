#!/usr/bin/env python3

import os
import sys

class Test:
    def __init__(self):
        pass

    def __call__(self):
        #  os.close(1)

        f = open("/tmp/test.file", "w")
        os.dup2(f.fileno(), 1)
        #  os.dup2(f.fileno(), 2)
        print("======> ", f.fileno(), file=open("/dev/pts/22", "w"))
        #  os.close(f.fileno())

        print("hello %d world %s %x" % (11, "kyo", 1000))

        w = open("/tmp/test.file")
        print(w.fileno())
        w.close()

        e = open("/tmp/test.file")
        print("3 open: ", e.fileno(), file=sys.stderr)


if __name__ == "__main__":
    Test()()
