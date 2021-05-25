#!/usr/bin/env python3

def run(*n1, **n2):
    print("run: ", n1, n2)

#  def test(a, b=(), k={}):
#  def test(a, *args, **kwargs):

def test(a, *b, **k):
    print("test a = ", a, ", b = ", b, ", k = ", k)
    a(*b, **k)

def main():
    c = (34, 56)
    test(run, 1, n2=2, n3=67)

if __name__ == "__main__":
    main()
