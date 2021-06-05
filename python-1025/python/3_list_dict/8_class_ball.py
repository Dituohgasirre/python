#!/usr/bin/env python3


import time
import os
import kyo.vt as vt
from kyo.term import Term
from threading import Thread
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


class Shape:
    """
    形状
        属性:
            画布实例对象 坐标 宽高 样式(颜色和字符)

        行为:
            初始化操作
            作画/显示
            移动
            改变样式
    """

    def __init__(self, canvas, **kargs):
        self.canvas = canvas
        w, h = canvas.size()
        self.__dict__.update(kargs)
        self.w = getattr(self, 'w', 1)
        self.h = getattr(self, 'h', 1)

        self.r = getattr(self, 'r', randint(1, h - self.h - 1))
        self.c = getattr(self, 'c', randint(1, w - self.w - 1))

        self.color = getattr(self, 'color', canvas.getColor())

    def setSize(self, w=1, h=1):
        self.w = w
        self.h = h
        self.r = self.r - self.h if self.r > self.h else self.r
        self.c = self.c - self.w if self.c > self.w else self.c
        return self

    def setColor(self, color=None):
        self.color = self.canvas.getColor() if color is None else color
        return self

    def setPos(self, r=None, c=None):
        w, h = self.canvas.size()
        self.r = randint(1, h - 2) if r is None else r
        self.c = randint(1, w - 2) if c is None else c
        return self

    def draw(self):
        w, h = self.canvas.size()
        for i in range(self.h):
            for j in range(self.w):
                r, c = self.r + i, self.c + j

                if r <= 0 or r >= h or c <= 0 or c >= w:
                    continue
                self.canvas[r][c] = self

    def cors(self, r=None, c=None):
        r = r or self.r
        c = c or self.c
        x = set()
        for i in range(self.h):
            for j in range(self.w):
                x.add((r + i, c + j))
        return x


class Ball(Shape):
    """
    球(形状):
        属性:
            步长

        行为:
            初始化操作
            移动
            改变步长
    """
    def __init__(self, canvas, **kargs):
        Shape.__init__(self, canvas, **kargs)
        self.r_inc = getattr(self, 'r_inc', choice((1, -1)))
        self.c_inc = getattr(self, 'c_inc', choice((1, -1)))

    def bounce(self):
        w, h = self.canvas.size()
        if self.r + self.r_inc < 1 or self.r + self.h + self.r_inc > h - 1:
            self.r_inc = -self.r_inc

        if self.c + self.c_inc < 1 or self.c + self.w + self.c_inc > w - 1:
            self.c_inc = -self.c_inc

    def predict(self):
        r = self.r + self.r_inc
        c = self.c + self.c_inc
        return self.cors(r, c)

    def hit(self, obstacle):
        return bool(self.predict() & obstacle.cors())

    def move(self):
        self.r += self.r_inc
        self.c += self.c_inc

    def __str__(self):
        return getattr(self, 'ch', '@')

    def __radd__(self, s):
        return s + str(self)


class Obstacle(Shape):
    """
    障碍物(形状):
        行为:
            初始化操作
            移动
    """
    def __init__(self, canvas, **kargs):
        Shape.__init__(self, canvas, **kargs)
        self.count = 0
        self.total = getattr(self, 'total', randint(10, 50))

    def __str__(self):
        return getattr(self, 'ch', '+')


class Pinball(Canvas, Thread):
    """
    弹球基类(画布, 线程)
        属性:
            球的列表
            障碍物列表
            球和障碍物的个数
            暂停/退出标识符

        行为:
            初始化操作(__init__)
            重写线程类的run实现弹球动画
            重写线程类的start实现弹球程序控制
    """
    def __init__(self, args=None, **kargs):
        args, opt = parse(['w|width|1',
                           'h|height|1',
                           'n|num|1',
                           'o|obs|1',
                           's|speed|1'], args)

        width = int(opt['width']) if 'width' in opt else 80
        height = int(opt['height']) if 'height' in opt else 20
        self.num = int(opt['num']) if 'num' in opt else 1
        self.speed = float(opt['speed']) if 'speed' in opt else 0.1
        self.obsNum = int(opt['obs']) if 'obs' in opt else 0

        Canvas.__init__(self, width, height, **kargs)
        Thread.__init__(self, daemon=True)

        self.quit = False
        self.pause = False
        self.balls = [Ball(self) for x in range(self.num)]
        self.obstacles = [Obstacle(self) for x in range(self.obsNum)]

    def exit(self):
        self.quit = True
        self.join()

    def draw(self):
        for ball in self.balls:
            ball.draw()

        for obs in self.obstacles:
            obs.draw()

    def move(self):
        for ball in self.balls:
            ball.bounce()
            for obs in self.obstacles:
                if ball.hit(obs):
                    ball.r_inc = -ball.r_inc
                    ball.c_inc = -ball.c_inc
            ball.move()

    def start(self):
        Thread.start(self)

    def run(self):
        while not self.quit:
            if not self.pause:
                self.init()
                self.draw()
                self.move()
                self.show()
            time.sleep(self.speed)


class VtBall(Pinball, vt.Vt, Term):
    """
    Vt码弹球类(弹球基类, Vt, Term):
        实现析构函数(__del__) 弹球退出时的操作
        重写线程类的start实现弹球程序控制
    """

    def __init__(self, args=None, **kargs):
        Pinball.__init__(self, args, **kargs)
        vt.Vt.__init__(self)
        Term.__init__(self)
        self.hide().screen()

        for b in self.balls:
            b.ch = chr(randint(33, 126))
            b.setSize(3, 3)

        for o in self.obstacles:
            #  o.ch = chr(randint(33, 126))
            o.ch = '#'
            o.setSize(5, 5)

    def exit(self):
        vt.Vt.show(False)
        Term.exit(self)
        Pinball.exit(self)

    def show(self, out=True):
        self.goto(back=False)
        for r in self:
            for c in r:
                if c == self.content or c == self.border:
                    print(c, end='')
                else:
                    self.out(c, c.color, back=False)
            print()
        #  return Canvas.show(self, out)

    def start(self):
        Pinball.start(self)
        while True:
            ch = Term.get(self)
            if ch == 'q':
                self.quit = True
                break
            elif ch == ' ':
                self.pause = not self.pause
            elif ch == 'c':
                for b in self.balls:
                    b.setColor()
        self.exit()

    def getColor(self):
        return vt.Vt.get()


#  Pygame弹球类(弹球基类, Gui):

if __name__ == "__main__":
    VtBall().start()

