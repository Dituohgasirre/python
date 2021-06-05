#!/usr/bin/env python3


import os
import time
from random import random, choice
from multiprocessing import *


def work(name):
    for i in range(10):
        print("work %s pid = %d" % (name, os.getpid()))
        time.sleep(choice((1, 2, 3, 4, 5)))

def do(a, b, i):
    print("do pid = %d, args(%d, %d)" % (os.getpid(), a, b))
    work("do[%d]" % i)


if __name__ == "__main__":
    def main():
        print("main pid = %d" % os.getpid())
        p = Pool(3)
        for i in range(10):
            p.apply_async(do, (11, 22, i))
        work("main")
        p.close()

    main()
