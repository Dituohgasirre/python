#!/usr/bin/env python3

g = 10

def main():
    e = 99
    def sub():
        global g
        nonlocal e
        l = 77
        #  print("sub l = ", l, ", e = ", e, ", g = ", g, ", list = ", list)
        print("sub l = %d, e = %d, g = %d, list = %s" % (l, e, g, list))
        l = 34
        e = 88
        g = 100
        print("edit sub l = %d, e = %d, g = %d, list =%s" % (l, e, g, list))
        #  import builtins as b
        b = __import__('builtins')
        print("list = ", b.list)

    sub()
    print("main e = %d, g = %d, list = %s" % (e, g, list))

if __name__ == "__main__":
    main()
    print("g = ", g)
