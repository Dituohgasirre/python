#!/usr/bin/env python3


import time
import os
import kyo.vt as vt
from kyo.term import Term
from random import randint, choice
from pargs import parse


class Canvas:
    """
    画布类
    #  属性:
        #  宽高 -> 二维数组
        #  边框字符
        #  画布字符

    #  行为/方法:
        #  初始化操作
        #  作画
            #  def draw(self, x, y, data):
                #  self.data[x][y] = data
        #  获取大小
        #  刷新画布
    """

    def __init__(self, width, height, **kargs):
        self.width, self.height = width, height
        self.border = '#'
        self.content = ' '
        self.__dict__.update(kargs)

        self.data = [[self.content] * self.width for x in range(self.height)]
        self.init()

    def init(self):
        for r in range(self.height):
            for c in range(self.width):
                if (r == 0 or c == 0
                        or r == self.height - 1 or c == self.width - 1):
                    self.data[r][c] = self.border
                else:
                    self.data[r][c] = self.content
        return self

    def __getitem__(self, index):
        return self.data[index]

    def size(self):
        return self.width, self.height

    def show(self, out=True):
        s = ""
        for r in self.data:
            for c in r:
                s += c
            s += "\n"

        if out == True:
            print(s)
            return self
        return s

    def __str__(self):
        return self.show(False)

    def __radd__(self, s):
        return s + str(self)

class FiveChess(Canvas):

    def __init__(self, args=None, **kargs):
        args, opt = parse(['w|width|1', 'h|height|1'], args)

        width = int(opt['width']) if 'width' in opt else 21
        height = int(opt['height']) if 'height' in opt else 11
        Canvas.__init__(self, width, height, border='+', content='+', **kargs)

        self.r = height // 2
        self.c = width // 2
        self.turn = '#'

    def checkWin(self, sx, sy):
        """
        五子棋输赢判断算法
        """
        old = -1
        y = self.r - sy * 4
        x = self.c - sx * 4

        for i in range(9):
            if (not (y < 0 or x < 0
                           or y >= self.height
                           or x >= self.width)):
                if old == self.data[y][x]:
                    count += 1
                else:
                    count = 1
                    old = self.data[y][x]

                if old and count == 5:
                    return True
            y += sy
            x += sx

        return False

    def press(self):
        if self.data[self.r][self.c] != '+':
            return

        self.data[self.r][self.c] = self.turn

        #  输赢判断
        if (self.checkWin(1, 0) or self.checkWin(0, 1)
             or self.checkWin(1, 1) or self.checkWin(1, -1)):
            return 1

        #  和棋判断
        for r in self.data:
            for c in r:
                if c == '+':
                    self.turn = '#' if self.turn == '@' else '@'
                    return 0

        return 2

class VtChess(FiveChess, vt.Vt, Term):

    def __init__(self, args=None, **kargs):
        FiveChess.__init__(self, args, **kargs)
        vt.Vt.__init__(self)
        Term.__init__(self)
        self.cout().screen().goto()
        self.show()

    def show(self, out=True):
        self.goto()
        for r in self.data:
            for c in r:
                print(c, end='')
            print()
        self.goto(self.r + 1, self.c + 1, back=False)

    def handle(self):
        c = Term.get(self)
        if c == 'q':
            break
        elif c == 'w' and self.r > 0:
            self.r -= 1
        elif c == 's' and self.r < self.height - 1:
            self.r += 1
        elif c == 'a' and self.c > 0:
            self.c -= 1
        elif c == 'd' and self.c < self.width - 1:
            self.c += 1
        elif c == ' ':
            ret = self.press()
            if ret == 1:
                print("羸了...")
                break
            elif ret == 2:
                print("和...")
                break

    def recv(self):
        data, addr = packet.recv()
        self.data = data['data']
        self.r = data['r']
        self.c = data['c']
        self.turn = data['turn']

    def send(self):
        data = {}
        data['data'] = self.data
        data['r'] = self.r
        data['c'] = self.c
        data['turn'] = self.turn
        packet.send(data, addr, Packet.DATA)

    def run(self):
        while True:
            if self.turn != '#':
                self.recv()
            else:
                self.handle()
                self.send()

            self.show()


if __name__ == "__main__":
    c = VtChess()
    c.run()

