#!/usr/bin/env python3

import kyo.menu
import win
import pygame

class Menu(kyo.menu.Menu):
    def __init__(self, **kwargs):
        self.cur = 0
        super().__init__(**kwargs)

    def show(self, *args, **kwargs):
        x = self.pos[0]
        y = self.pos[1]
        for i, t in enumerate(self.items):
            if self.cur == i:
                self.screen.blit(t.title[0], (x, y))
            else:
                self.screen.blit(t.title[1], (x, y))
            y += t.title[0].get_height()
        win.flip()


    def input(self, prompt="", *args, **kwargs):
        return pygame.event.wait()


    def run(self, e, *args, **kwargs):
        if e.type == pygame.QUIT:
            return True
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                return True
            elif e.key == pygame.K_w:
                if self.cur > 0:
                    self.cur -= 1
                pass
            elif e.key == pygame.K_s:
                if self.cur < self.itemLen - 1:
                    self.cur += 1
            elif e.key == pygame.K_RETURN:
                return self.items[self.cur].run(self.cur)

            self.show()


if __name__ == "__main__":
    def main():
        def func(i, args):
            print("pymenu func: ", i, args)

        pg = win.create()
        font = pygame.font.Font("/kyo/demo/box/simfang.ttf", 20)
        m = Menu(title="Pygame的菜单", screen=win.screen(), pos=(100, 100))

        p = pygame.image.load("/kyo/python/4_pygame/player.bmp")
        p.set_colorkey((247, 0, 255))
        p1 = p.subsurface((0, 0, 48, 48))
        p2 = p.subsurface((0, 48, 48, 48))
        p3 = p.subsurface((0, 48 * 2, 48, 48))

        m.add(p1, func, foucs=p2)
        m.add(p2, func, foucs=p2)
        m.add(p3, func, foucs=p2)

        fg = (255, 0, 0)
        fcolor = (0, 0, 255)
        t11 = font.render("创建游戏", True, fg)
        t12 = font.render("创建游戏", True, fcolor)

        t21 = font.render("加入游戏", True, fg)
        t22 = font.render("加入游戏", True, fcolor)

        t31 = font.render("退出游戏", True, fg)
        t32 = font.render("退出游戏", True, fcolor)


        m.add(t11, func, args=(pg, m), foucs=t12)
        m.add(t21, func, args=(pg, m), foucs=t22)
        m.add(t31, func, args=(pg, m), foucs=t32)
        m.loop()

    main()
