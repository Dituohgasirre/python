#!/usr/bin/env python3

#  封装菜单
    #  菜单条目类
        #  显示对象(文本　图片)
        #  触发条目执行的操作 -> 用户数据的传递
        #  菜单条目类有可能是子菜单

    #  菜单类  --> 整个菜单功能
        #  包含多个菜单条目的实例对象 -> 列表存储 -> 核心数据
        #  核心功能　-> 操作包含多个菜单条目的实例对象
            #  添加菜单条目 --> add
            #  修改菜单条目
            #  删除菜单条目
            #  查找菜单条目 --> loop -> show -> input -> run

        #  实现子菜单功能
            #  子菜单缩进显示
            #  返回上一级
            #  退出整个菜单


class Item:
    def __init__(self, title, call=None, args=None, **kwargs):
        self.title = title
        self.name = None
        self.id = None
        self.call = call
        self.args = args
        self.__dict__.update(kwargs)

    def isMenu(self):
        return isinstance(self.call, Menu)

    def getMenu(self):
        return self.call if self.isMenu() else None

    def __str__(self):
        return self.title if type(self.title) == str else ""

    def run(self, usrInput):
        if self.call is None:
            return True
        return self.call(usrInput, self.args)


class Menu:
    @staticmethod
    def back(i=None, args=None):
        return True

    @staticmethod
    def exit(i=None, args=None):
        while args:
            args.quit = True
            args = args.parent
        return True

    def __init__(self, **kwargs):
        self.title = None
        self.items = []
        self.itemLen = 0
        self.parent = None
        self.quit = False
        self.level = 0
        self.isIndent = True
        self.__dict__.update(kwargs)

        if self.parent is not None:
            self.level = self.parent.level + 1


    def addBack(self, title="返回上一级"):
        return self.add(title, call=Menu.back)

    def addExit(self, title="退出程序"):
        return self.add(title, call=Menu.exit, args=self.parent)


    def add(self, obj, call=None, args=None, **kwargs):
        """
            添加菜单条目
            @param obj      菜单条目实例对象(Item), 不为Item实例对象自动打包
            @param call     菜单条目触发操作, None为退出菜单
            @param args     菜单条目触发操作的数据
            @param kwargs   菜单条目扩展数据
            例:
                m.add(Item(title, call, args))
                m.add("title", call, args)
        """
        if not isinstance(obj, Item):
            return self.add(Item(obj, call, args, **kwargs))

        self.items.append(obj)
        self.itemLen += 1

        #  以下代码为了父菜单添加子菜单的情况
        #  子菜单的父菜单如果确定关系则不会执行以下代码
        subMenu = obj.getMenu()
        if subMenu is not None and subMenu.parent != self:
            subMenu.parent = self
            subMenu.level = self.level + 1

        return self

    def show(self, *args, **kwargs):
        if 'hookShow' in self.__dict__:
            return self.hookShow(self)
        indentStr = "  " * self.level if self.isIndent else ""

        if self.title is not None:
            print(indentStr, self.title)

        for i, item in enumerate(self.items):
            print("%s%d.%s" % (indentStr, i + 1, item))

        return "%s请输入[1 - %d]: " % (indentStr, self.itemLen)

    def input(self, prompt="", *args, **kwargs):
        while True:
            try:
                num = int(input(prompt))
            except:
                continue

            if 1 <= num <= self.itemLen:
                break

        return num


    def run(self, usrInput, *args, **kwargs):
        return self.items[usrInput - 1].run(usrInput)


    def loop(self, *args, **kwargs):
        while not self.run(self.input(self.show())):
            pass

        return False if self.parent is None else self.parent.quit


    def __call__(self, *args, **kwargs):
        return self.loop(*args, **kwargs)


if __name__ == "__main__":
    def main():
        def func(i, args):
            print("---------> func: ", i, args)

        def myShow(m):
            print("接管一级菜单显示: ", m.title, sep='')
            n = 1
            for i in m.items:
                print("\033[34m", n, ".", i, "\033[0m", sep='')
                n += 1
            return "\033[34m请输入: "

        m = Menu(title="\033[31m一级菜单标题\033[0m", hookShow=myShow)
        sm = Menu(title="\033[32m二级菜单标题\033[0m", parent=m)
        ssm = Menu(title="三级菜单标题", parent=sm)

        it = Item("通用菜单项", func, "通用菜单项的数据")

        ssm.add(it)
        ssm.add(Item("aaaaa", call=func, args="aaaaa"))
        ssm.add(Item("bbbbb", call=func, args="bbbbb"))
        ssm.add(Item("ccccc", call=func, args="ccccc"))
        ssm.addBack().addExit()

        sm.add(it)
        sm.add("AAAAA", call=ssm)
        sm.add("BBBBB", call=func, args="BBBBB")
        sm.add("CCCCC", call=func, args="CCCCC")
        sm.addBack().addExit()

        m.add(it)
        m.add(Item("11111", call=sm))
        m.add(Item("22222", call=func, args="第二个菜单项"))
        m.add(Item("33333", call=func, args="第三个菜单项"))
        m.add(Item("44444", call=func, args="第四个菜单项"))
        m.addExit("exit")

        m.loop()

    main()
