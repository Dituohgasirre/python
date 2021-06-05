#!/usr/bin/env python3

def test():
    a = 1
    a += 1
    return a

def main():
    a = 0
    print("main....")
    def sub():
        nonlocal a
        print("sub a = ", a)
        a += 1
        return a

    return sub


if __name__ == "__main__":
    s = main()
    s1 = main()

    print(s())
    print(s())
    print(s())

    print(s1())
    print(s1())
    print(s1())

    #  print(test())
    #  print(test())
    #  print(test())
    #  print(test())
