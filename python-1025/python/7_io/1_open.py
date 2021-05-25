#!/usr/bin/env python3

import sys
import time


class Test:
    def __init__(self):
        pass

    def __call__(self, s="world"):
        f = open("/tmp/test.file", "rb+")
        data = f.read(5)
        print(data, type(data), f.tell())

        data = f.read(5)
        print(data, type(data), f.tell())

        #  f.seek(-5, 2)
        #  print("seek = ", f.tell())

        ret = f.write(s.encode())
        f.flush()
        print("write ret = %d" % ret)
        time.sleep(10)
        f.close()



if __name__ == "__main__":
   Test()(sys.argv[1])
