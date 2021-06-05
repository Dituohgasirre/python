#!/usr/bin/env python3

import os
import time

s = 100

if __name__ == "__main__":
    def main():
        global s
        if os.fork() == 0:
            print("child run s = %d %d ..... pid = %d, ppid = %d"
                        % (s, id(s), os.getpid(), os.getppid()))
            s += 100
            time.sleep(10)
            os._exit(99)

        pid, status = os.wait()
        if os.WIFEXITED(status):
            print("自杀 status = %d s = %d " % (os.WEXITSTATUS(status), s))
        elif os.WIFSIGNALED(status):
            print("被人杀死...")
            #  main()
        print("pid = ", pid, ", status = ", status)

    print("main: ", s, id(s))
    main()
