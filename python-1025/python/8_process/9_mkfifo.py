#!/usr/bin/env python3


import os
import time


if __name__ == "__main__":
    def main():

        filename = "/tmp/fifo"
        if not os.path.exists(filename):
            os.mkfifo(filename)

        if not os.fork():
            print("child run....")
            fd = open(filename, "w")
            time.sleep(3)
            fd.write("hello parent")
            fd.flush()
            os._exit(0)

        fd = open(filename, "r")
        print("read child data: ", fd.read())


    main()
