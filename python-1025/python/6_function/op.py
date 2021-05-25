#!/usr/bin/env python3

import os
import sys

def main():
    o = {}

    sys.path.append("./kyo")
    for f in os.listdir("./kyo"):
        if f.endswith(".py"):
            o.update( __import__(f[:-3]).op)

    for i in o:
        for j in o:
            if o[i](o[j](5, 3), 2) == 4:
                print("(5 %s 3) %s 2 = 4" % (j, i))

if __name__ == "__main__":
    main()
