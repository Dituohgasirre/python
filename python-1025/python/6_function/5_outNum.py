#!/usr/bin/env python3

import sys

def outNum(num, bit=16, end='\n'):
    #  def _outNum(num, bit):
        #  if num == 0:
            #  return ''
        #  return _outNum(num // bit, bit) + '0123456789ABCDEF'[num % bit]

    #  def _outNum(num, bit):
        #  s = ''
        #  while num != 0:
            #  s += '0123456789ABCDEF'[num % bit]
            #  num //= bit
        #  return s[::-1]

    def _outNum(num, bit):
        stack = []

        while num != 0:
            stack.append('0123456789ABCDEF'[num % bit])
            num //= bit

        s = ''
        while stack:
            s += stack.pop()

        return s

    try:
        start = {2: '0b', 8: '0o', 16: '0x'}[bit]
    except:
        start = ''

    if num == 0:
        start += '0'
    if num < 0:
        start = '-' + start
        num = -num

    return start + _outNum(num, bit) + end

def main():
    sys.stdout.write(outNum(0, 2))

    sys.stdout.write(outNum(10, 3))

    sys.stdout.write(outNum(-10, 2))

    sys.stdout.write(outNum(180, 2))
    #%o
    sys.stdout.write(outNum(180, 8))
    #%d
    sys.stdout.write(outNum(180, 10))
    #%x
    sys.stdout.write(outNum(180, 16))

if __name__ == "__main__":
    main()
