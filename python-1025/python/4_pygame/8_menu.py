#!/usr/bin/env python3

from kyo.pgmenu import Menu
import win
import pygame

class MenuTest:
    def loadImgRes(self):
        p = pygame.image.load("/kyo/python/4_pygame/player.bmp")
        p.set_colorkey((247, 0, 255))

        self.imgRes = []
        i = 0
        while i < 11:
            if i == 8:
                i += 1
                continue
            data = [None, None]
            data[0] = p.subsurface((0, i * 48, 48, 48))
            data[1] = p.subsurface((0, (i + 1) * 48, 48, 48))
            self.imgRes.append(data)
            i += 2

    def loadTxtRes(self, txtlist, color, foucs_color):
        self.txtRes = []
        for txt in txtlist:
            data = [None, None]
            data[0] = self.font.render(txt, True, color)
            data[1] = self.font.render(txt, True, foucs_color)
            self.txtRes.append(data)


    def __init__(self):
        self.pg = win.create()
        self.font = pygame.font.Font("/kyo/demo/box/simfang.ttf", 20)

        self.m = Menu(screen=win.screen(), pos=(100, 100))
        self.sm = Menu(screen=win.screen(), pos=(300, 100), parent=self.m)

        txtlist = ["创建游戏", "加入游戏", "单机游戏", "退出游戏"]
        callist = [self.sm,
                   lambda i, a: print("加入游戏的执行函数"),
                   lambda i, a: print("单机游戏的执行函数"),
                   lambda i, a: True]
        self.loadTxtRes(txtlist, win.toColor(0xFFFFFF), win.toColor(0xFF0000))
        self.loadImgRes()

        for img in self.imgRes:
            self.sm.add(img, lambda i, a: print("子菜单条目执行的函数"))

        callIt = iter(callist)
        for txt in self.txtRes:
            self.m.add(txt, next(callIt))

    def run(self):
        self.m.loop()
        pass

    def __call__(self):
        return self.run()


if __name__ == "__main__":
    MenuTest()()

