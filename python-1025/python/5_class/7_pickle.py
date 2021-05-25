#!/usr/bin/env python3

import pickle
import shelve as sh

class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s %d" % (self.name, self.age)

if __name__ == "__main__":
    #  c = Test("张三", 20)
    #  pickle.dump(c, open("./test.db", "wb"))
    c = pickle.load(open("./test.db", "rb"))
    print(c)

    #  s = sh.open("./testsh.db")
    #  s['num'] = 3678
    #  s['list'] = [3, 6, 7, 8, 9, 9]
    #  s['obj'] = c
    #  s.close()
    s = sh.open("./testsh.db")
    print(s['num'])
    l = s['list']
    print(l)
    c = s['obj']
    print(c)
    s.close()

