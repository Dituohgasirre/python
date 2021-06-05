#!/usr/bin/env python3


import os
import time


if __name__ == "__main__":
    def main():
        pid = os.fork()
        if not os.fork():
            print("1 child start pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
            time.sleep(10)
            print("2 child start pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
            time.sleep(100)
            print("child end!")
            os._exit(0)
        print("parent end...")
        #  print("child wait: ", os.wait())
        #  time.sleep(100)


    main()
