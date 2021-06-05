#!/usr/bin/env python3


import os
import time
from random import random
from multiprocessing import *

def do(a, b, q):
    print("do pid = %d, args(%d, %d)" % (os.getpid(), a, b))
    l = q.get()
    l.append(111)
    l.append(111)
    l.append(111)
    q.put(l)
    print("do l: ", l)
    time.sleep(1)


if __name__ == "__main__":
    def main():
        print("main pid = %d" % os.getpid())
        q = Queue(3)
        l = []
        print("l = ", l)
        q.put(l)
        p = Process(target=do, args=(11, 22, q))
        p.start()
        p.join()
        l = q.get()
        print("main: ", l)

    main()
