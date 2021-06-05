#!/usr/bin/env python3


import os
import time
import signal


if __name__ == "__main__":
    def sig_handle(num, info):
        print("sig ....., num = ", num, ", info = ", info)

    def main():
        signal.signal(signal.SIGHUP, signal.SIG_IGN)
        signal.signal(signal.SIGINT, sig_handle)

        print("pid = %d" % os.getpid())
        time.sleep(10000)

    main()
