#!/usr/bin/env python3


import os
import time


if __name__ == "__main__":
    def main():

        rd, wd = os.pipe()

        if not os.fork():
            os.close(rd)
            print("child run....")
            time.sleep(3)
            os.write(wd, b"hello")
            os._exit(0)

        os.close(wd)
        print("read child data: ", os.read(rd, 1024))


    main()
