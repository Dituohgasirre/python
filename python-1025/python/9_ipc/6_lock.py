#!/usr/bin/env python3


import os
import time
from random import random
from multiprocessing import *


def do(name, f, l):
    print("do pid = %d, name = %s" % (os.getpid(), name))
    for i in range(100):
        s = "work %s pid = %d count = %d\n" % (name, os.getpid(), i)
        l.acquire()
        for c in s:
            f.write(c)
            f.flush()
            time.sleep(0.001)
        l.release()


if __name__ == "__main__":
    def main():
        f = open("/tmp/testfile", "w")
        l = Lock()
        print("main pid = %d" % os.getpid())
        p = Process(target=do, args=("do", f, l))
        p.start()
        do("main", f, l)

    main()
