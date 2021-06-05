#!/usr/bin/env python3


import sys
import os
import time


if __name__ == "__main__":
    print("test Run pid = %d.... uid = %d" % (os.getpid(), os.getuid()))
    print(os.environ)
    if 'KYO' in os.environ:
        print("KYO ENV = ", os.environ['KYO'])
    print(sys.argv)
    time.sleep(100)
    print("test Exit....")
