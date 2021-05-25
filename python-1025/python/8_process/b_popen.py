#!/usr/bin/env python3


import os


if __name__ == "__main__":
    def fifoCmd():
        rd, wd = os.pipe()

        if not os.fork():
            os.dup2(rd, 0)
            os.execlp("grep", "grep", "root", "--color")

        os.dup2(wd, 1)
        os.execlp("cat", "cat", "/etc/passwd")


    def popenTest():
        r = os.popen("cat /etc/passwd")
        w = os.popen("grep root --color", 'w')

        w.write(r.read())

        r.close()
        w.close()

    popenTest()
