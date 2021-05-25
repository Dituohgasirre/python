#!/usr/bin/env python3


import os
import sys
import time
import threading


class Term:

    o = None

    def __new__(obj, *args, **kargs):
        if Term.o is None:
            Term.o = object.__new__(obj)
        return Term.o

    def __init__(self):
        self.w, self.h = os.get_terminal_size()
        self.ctl()

    def exit(self):
        self.ctl(True)

    def ctl(self, val=False, name=['echo', 'icanon']):
        if type(name) == list:
            s = ""
            for x in name:
                s += "%s%s " % ("- "[val], x)
        else:
            s = "%s%s" % ("- "[val], name)

        os.system("stty " + s)

        return self

    def input(self, prompt="", types=str):
        self.ctl(True)
        s = input(prompt)
        self.ctl(False)
        return types(s)

    def __del__(self):
        self.exit()

    def get(self, num=1):
        return sys.stdin.read(num)

    @property
    def size(self):
        self.w, self.h = os.get_terminal_size()
        return self.w, self.h

    def sleep(self, sec=0.1):
        time.sleep(sec)
        return self

    @staticmethod
    def run(call, interval=None, args=None, kwargs=None):
        if interval is None:
            t = threading.Thread(target=call,
                                    args=args, kwargs=kwargs, daemon=True)
        else:
            t = threading.Timer(interval, call, args=args, kwargs=kwargs)
        t.start()
        return t


if __name__ == '__main__':
    g = Term()

    num = g.input("请输入一个数字: ", int)
    print(g.size, g.w, g.h, "num: ", num, type(num))

    def test(data):
        print("test data: ", data)
        g.sleep(5)
        print("test end")

    t = g.run(test, args=("hello", ))

    while True:
        ch = g.get()
        if ch == 'q':
            break

    g.exit()
    g = Term()


