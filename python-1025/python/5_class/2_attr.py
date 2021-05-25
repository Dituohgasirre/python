#!/usr/bin/env python3

class AttrTest:
    __name = "kyo"

    def __init__(self):
        self.__age = 23
        pass

    def getAge(self):
        return self.__age

    def __run(self):
        print("AttrTest Run")

    def __str__(self):
        return str(self)


if __name__ == "__main__":
   c = AttrTest()
   c.__age = 67
   print(c.__dict__, c.__age)
   #  c._AttrTest__run()

   print(c.getAge(), c._AttrTest__age)
