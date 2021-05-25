#!/usr/bin/env python3

import kyo.menu as menu
import kyo.vt as vt
import kyo.term as gt

class Menu(menu.Menu):
    def __init__(self, **kwargs):
        self.v = vt.Vt()
        self.g = gt.Term()
        self.wait = True
        self.disNum = 10
        self.disPage = 0

        self.cur = 0
        super().__init__(**kwargs)

        if 'initHook' in self.__dict__:
            self.initHook(self.v)
        else:
            self.v.run(vt.SCREEN, self.v.goto(), vt.HIDE)

        if "isIndent" not in kwargs:
            kwargs['isIndent'] = False


    def __del__(self):
        if 'delHook' in self.__dict__:
            self.delHook(self.v)
        else:
            self.v.run(vt.SHOW)
            #  self.v.run(vt.SHOW, self.v.goto(20))
        self.g.exit()

    def run(self, ch, *args, **kwargs):
        if ch == 'q':
            return self.exit(args=self.parent)
        if ch == chr(27):
            return True
        elif ch == 's' and self.cur < self.itemLen - 1:
            self.cur += 1
            if self.cur >= self.disNum:
                self.disPage += 1
        elif ch == 'w' and self.cur > 0:
            if self.cur == self.disPage:
                self.disPage -= 1
            self.cur -= 1
        elif ch == chr(10):
            self.v.run(vt.SCREEN, self.v.goto(), vt.SHOW)
            ret = self.items[self.cur].run(self.cur)
            if ret is None and self.wait:
                input("----　按回车继续 ----")
            self.v.run(vt.HIDE)
            return ret

        self.show()

    def input(self, prompt="", *args, **kwargs):
        return self.g.get()

    def show(self, *args, **kwargs):
        if 'hookShow' in self.__dict__:
            return self.hookShow(self)

        #  self.v.run(vt.SCREEN, self.v.goto())

        if self.title is not None:
            print(self.title)

        l  = self.itemLen if self.itemLen < self.disNum else self.disNum

        def _outItem(itemObj, index, menuObj):
            if index == menuObj.cur:
                print(menuObj.v.out(itemObj, unline=True))
            else:
                print(itemObj)

        call = self.hookOutItem if 'hookOutItem' in self.__dict__ else _outItem
        for i in range(l):
            s = i + self.disPage
            call(self.items[s], s, self)


if __name__ == "__main__":

    def main():
        def func(i, args):
            print("---------> func: ", i, args)

        Item = menu.Item

        m = Menu(title="菜单标题")
        sm = Menu(title="子菜单标题", parent=m)
        ssm = Menu(title="------子菜单标题", parent=sm)

        ssm.add("AAAAA", func, "AAAAA")
        ssm.add("BBBBB", func, "BBBBB")
        ssm.add("CCCCC", func, "CCCCC")

        sm.add("AAAAA", ssm)
        sm.add("BBBBB", func, "BBBBB")
        sm.add("CCCCC", func, "CCCCC")

        m.add("11111", sm)
        m.add("22222", func, "第二个菜单项")
        m.add("33333", func, "第三个菜单项")
        m.add("44444", func, "第四个菜单项")

        m.add("22222", func, "第二个菜单项")
        m.add("33333", func, "第三个菜单项")
        m.add("44444", func, "第四个菜单项")
        m.add("22222", func, "第二个菜单项")
        m.add("33333", func, "第三个菜单项")
        m.add("14444", func, "第四个菜单项")
        m.add("24444", func, "第四个菜单项")
        m.add("34444", func, "第四个菜单项")
        m.add("44444", func, "第四个菜单项")
        m.add("54444", func, "第四个菜单项")
        m.add("64444", func, "第四个菜单项")
        m.loop()

    main()
