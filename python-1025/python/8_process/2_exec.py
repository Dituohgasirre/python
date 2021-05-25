#!/usr/bin/env python3


import os


if __name__ == "__main__":
    def main():
        print("main start pid = %d.... uid = %d" % (os.getpid(), os.getuid()))
        pid = os.fork()
        if pid == 0:
            os.environ['KYO'] = "hello world"
            os.environ = {}
            os.setuid(1002)
            print("child code..... pid = %d, ppid = %d"
                        % (os.getpid(), os.getppid()))
            os.exec("./3_test.py", ["", "/usr", "/var"], {})
            os._exit(0)
        pid, status = os.wait()

        print("%d main end for pid = %d...." % (os.getpid(), pid))

    main()
