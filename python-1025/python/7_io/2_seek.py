#!/usr/bin/env python3

class Test:
    def __init__(self):
        pass

    def __call__(self):
        f = open("/tmp/test.file", "wb")

        f.truncate(100)
        print("start tell = ", f.tell())
        f.seek(10, 2)
        print("seek tell = ", f.tell())
        f.write("0".encode())

        f.close()


if __name__ == "__main__":
    Test()()
