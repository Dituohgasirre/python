#!/usr/bin/env python3

import random

#  VT码命令前缀
PR = '\033['

#  光标操作定义
SAVE, LOAD, HIDE, SHOW = 's', 'u', '?25l', '?25h'

#  清除操作定义
SCREEN, LINE, END = '2J', '2K', 'K'

#  颜色定义
BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE, DEFAULT = range(9)

#  方向定义
UP, DOWN, LEFT, RIGHT = "ABDC"

class Vt:
    def __init__(self):
        self.back = False

    def setBack(self, back=True):
        self.back = back
        return self

    def run(self, cmd):
        if type(cmd) == list:
            cmd = ["%s%s" % (['', PR][PR not in x], x) for x in cmd]
            print(''.join(cmd), end='', flush=True)
        else:
            if self.back:
                return PR + cmd
            print("%s%s" % (['', PR][PR not in cmd], cmd), end='', flush=True)

        return self

    #绝对定位
    def goto(self, r=1, c=1):
        return self.run("%d;%dH" % (r, c))

    #相对定位
    def move(self, direction=RIGHT, step=1):
        return self.run("%d%s" % (step, direction))

    def left(self, step=1):
        return self.move(LEFT, step)

    def right(self, step=1):
        return self.move(RIGHT, step)

    def up(self, step=1):
        return self.move(UP, step)

    def down(self, step=1):
        return self.move(DOWN, step)

    def save(self):
        return self.run(SAVE)

    def load(self):
        return self.run(LOAD)

    def hide(self):
        return self.run(HIDE)

    def show(self):
        return self.run(SHOW)

    # 清除操作
    def clear(self):
        return self.run(SCREEN)

    def clearLine(self):
        return self.run(LINE)

    def clearLineEnd(self):
        return self.run(END)

    #颜色输出
    def setColor(self, fg=DEFAULT, bg=DEFAULT, bold=False):
        if fg == DEFAULT and bg == DEFAULT:
            return self.run("0m")
        fgstr = [str(fg + 30)+';', ''][fg == DEFAULT]
        return self.run("%s%s%dm" % (['', '1;'][bold], fgstr, bg + 40))

    def color(self, s, fg, bg=DEFAULT, bold=False):
        if not self.back:
            self.setBack()

        s = self.setColor(fg, bg, bold) + s + self.setColor()
        if self.back:
            self.setBack(False)

        return self.run(s)

    def getColor(self):
        return random.choice([BLACK, RED, GREEN,
                              YELLOW, BLUE, PURPLE, CYAN, WHITE])

#  vt测试
if __name__ == "__main__":
    v = Vt()
    v.color("hello", DEFAULT, BLACK).color("hello", DEFAULT, BLACK, True)
    v.color("hello", RED).color("hello", RED, bold=True)
    v.clear().goto(1, 1).hide().down(3).right(10).color("hello world\n", RED)
    v.setColor(BLUE)
    print("1hello world")
    v.setColor()
    print("2hello world")
    v.color("3hello world", YELLOW, BLACK, True)
    input()
    v.run(SHOW)

