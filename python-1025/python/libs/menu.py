#!/usr/bin/env python3

import sys

class Menu:
    def __init__(self, title="菜单标题"):
        self.items = []
        self.title = title

    def add(self, itemTitle, call=None, args=None):
        data = {}
        data['title'] = itemTitle
        data['call'] = call
        data['args'] = args

        self.items.append(data)

        return self

    def run(self, fixed=None):
        itemLen = len(self.items)

        items = self.items

        while True:
            try:
                if callable(fixed):
                    print("\033[2J\033[1;1H", end="", flush=True)

                print(self.title)

                for i, s in enumerate(self.items):
                    print("%d. %s" % (i + 1, s['title']))

                num = int(input("请输入[1 - %d]: " % itemLen)) - 1

                call = items[num]['call']

                if (not callable(call) or call(num, items[num]['args'])
                        or (callable(fixed) and fixed(num, items[num]['args']))):
                    break
            except:
                print("\033[1;31m错误: ", sys.exc_info()[1])
                input("\033[0m回车继续....")

#------------------------------------------------------------------------------

def add(title, call=None, args=None, items=None):
    """
    组合菜单项
    """
    if not isinstance(items, Menu):
        items = Menu()

    items.add(title, call, args)

    return items


def run(items, title=None, fixed=None):
    """
    运行菜单
    """
    items.run(fixed)


def main():
    def func(index, args):
        print("index = %d, args = %s" % (index, args))

    def end(index, args):
        print("--------------------------------------------")
        print("本题测试完成, 回车继续, q为退出: ", end='')
        return True if input() == 'q' else False

    #  没有实现类的测试
    #  menu = add("1111111", func, "tom")
    #  add("2222222", func, "mary", menu)
    #  add("3333333", func, "kyo", menu)
    #  add("exit", items=menu)

    #  run(menu, fixed=end)

    m = Menu("测试菜单类")
    m.add("111111", func, "tom")
    m.add("22222", func, "mary")
    m.add("333333", func, "kyo")
    m.add("exit")
    m.run(end)

    #  可以简写以下:

    #  (Menu("测试菜单类").add("111111", func, "tom")
                      #  .add("22222", func, "mary")
                      #  .add("333333", func, "kyo")
                      #  .add("exit").run(end))

if __name__ == "__main__":
    main()
