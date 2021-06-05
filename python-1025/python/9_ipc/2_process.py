#!/usr/bin/env python3


import os
import time
from random import random
from multiprocessing import *


def work(name):
    for i in range(10):
        print("work %s pid = %d" % (name, os.getpid()))
        time.sleep(random())

def do(a, b, i):
    print("do pid = %d, args(%d, %d)" % (os.getpid(), a, b))
    work("do[%d]" % i)


if __name__ == "__main__":
    def main():
        print("main pid = %d" % os.getpid())
        for i in range(10):
            p = Process(target=do, args=(11, 22, i))
            p.start()
        work("main")

    main()
