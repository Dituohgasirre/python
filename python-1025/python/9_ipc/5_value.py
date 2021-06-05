#!/usr/bin/env python3


import os
import time
from random import random
from multiprocessing import *

def do(a, b, v, arr):
    print("do pid = %d, args(%d, %d)" % (os.getpid(), a, b))
    print("do v: ", v.value)
    v.value = 99
    print(list(arr))
    arr[0] = 'H'.encode()
    time.sleep(1)


if __name__ == "__main__":
    def main():
        print("main pid = %d" % os.getpid())
        v = Value('d', 55)
        a = Array('c', 20)
        s = "hello world"
        for i, d in enumerate(s):
            a[i] = d.encode()
        p = Process(target=do, args=(11, 22, v, a))
        p.start()
        p.join()
        print("main: ", v.value, list(a))

    main()
