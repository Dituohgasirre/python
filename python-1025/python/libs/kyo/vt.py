#!/usr/bin/env python3


from random import choice


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

    o = None
    back = True

    def __new__(obj, *args, **kargs):
        if Vt.o is None:
            Vt.o = object.__new__(obj)
        return Vt.o

    @staticmethod
    def cout():
        """
        链式调用起点
        """
        Vt.back = False
        return Vt

    @staticmethod
    def endl():
        """
        链式调用终点
        """
        Vt.back = True
        return Vt

    @staticmethod
    def run(*cmd, back=False, end=""):
        """
        VT码实际操作函数
        @param cmd  位置可变参, 接受VT码命令来执行
        @param back 是否返回组合命令字符串, 默认不返回, 直接运行
        @param end  控制命令运行成功输出的结束符

        直接运行run函数默认不返回, 其它函数调用则传递None
        """
        if back is None:
            back = Vt.back

        #  print(["%s%s" % (['', PR][PR not in x], x) for x in cmd])
        cmds = ''.join(["%s%s" % (['', PR][PR not in x], x) for x in cmd])

        if back:
            return cmds

        print(cmds, end=end, flush=True)

        return Vt


    @staticmethod
    def goto(r=1, c=1, back=None):
        """
        绝对定位
        """
        return Vt.run("%d;%dH" % (r, c), back=back)

    @staticmethod
    def move(direction=RIGHT, step=1, back=None):
        """
        相对定位
        """
        return Vt.run("%d%s" % (step, direction), back=back)

    @staticmethod
    def left(step=1, back=None):
        """
        向左移动
        """
        return Vt.move(LEFT, step, back=back)

    @staticmethod
    def right(step=1, back=None):
        """
        向右移动
        """
        return Vt.move(RIGHT, step, back=back)

    @staticmethod
    def up(step=1, back=None):
        """
        向上移动
        """
        return Vt.move(UP, step, back=back)

    @staticmethod
    def down(step=1, back=None):
        """
        向下移动
        """
        return Vt.move(DOWN, step, back=back)

    @staticmethod
    def save(back=False):
        """
        保存光标
        """
        return Vt.run(SAVE, back=back)

    @staticmethod
    def load(back=False):
        """
        加载光标
        """
        return Vt.run(LOAD, back=back)

    @staticmethod
    def hide(back=False):
        """
        隐藏光标
        """
        return Vt.run(HIDE, back=back)

    @staticmethod
    def show(back=False):
        """
        显示光标
        """
        return Vt.run(SHOW, back=back)

    @staticmethod
    def screen(back=False):
        """
        清屏
        """
        return Vt.run(SCREEN, back=back)

    @staticmethod
    def line(back=False):
        """
        清除当前行
        """
        return Vt.run(LINE, back=back)

    @staticmethod
    def end(back=False):
        """
        清除光标之后内容
        """
        return Vt.run(END, back=back)

    @staticmethod
    def get():
        """
        随机获取颜色
        """
        return choice([BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE])

    @staticmethod
    def set(fg=DEFAULT, bg=DEFAULT, bold=False, unline=False, back=None):
        """
        设置影响光标之后文本颜色
        """
        if fg == DEFAULT and bg == DEFAULT and not bold and not unline:
            return Vt.run("0m", back=back)

        fg = [str(fg + 30)+';', ''][fg == DEFAULT]
        bold = ['', '1;'][bold]
        unline = ['', '4;'][unline]
        return Vt.run("%s%s%s%dm" % (bold, unline, fg, bg + 40), back=back)


    @staticmethod
    def out(s, fg=DEFAULT, bg=DEFAULT, bold=False, unline=False, back=None):
        """
        颜色输出对象
        """
        return Vt.run("%s%s%s" % (Vt.set(fg, bg, bold, unline, True),
                                  s, Vt.set(back=True)), back=back)

    @staticmethod
    def debug(r, msg, color=RED):
        """
        输出调试信息
        """
        return Vt.run(SAVE, Vt.goto(r), LINE, Vt.out(msg, color), LOAD)


#  vt测试
if __name__ == "__main__":
    v = Vt()
    #  print(v.goto(1, 1) + v.out("hello"))

    #  v.goto(1, 1, False).out("hello", back=False)

    v.cout().goto(1, 1).out("hello", bold=True, unline=True).endl()
    input()

    v.run(SCREEN, HIDE, v.goto(), v.out("hello"), end='\n').run(SHOW)
    v.debug(10, "hello world").hide()
    input()
    v.show()

    v.screen()
    v.goto(back=False)
    v.run(HIDE)

    v.out("hello", DEFAULT, BLACK, back=False)
    v.out("hello", DEFAULT, BLACK, True, back=False)
    v.out("hello", RED, back=False)
    v.out("hello", RED, bold=True, back=False)

    v.run(SCREEN, v.goto(), HIDE,
            v.down(3), v.right(10), v.out("0hello world\n", RED))

    v.set(BLUE, back=False)
    print("1hello world")
    v.set(back=False)
    print("2hello world")
    v.out("3hello world", YELLOW, BLACK, True, False)
    input()
    v.run(SHOW)

