#!/usr/bin/env python3

import menu

class Homework:
    def __init__(self):
        m = menu.Menu("==== 函数作业 ====")
        m.add("十进制转八进制", Homework.commonTest, {
                'prompt': "请输入十进制数及转换进制: ",
                'call': Homework.outNumTest
                })
        m.add("斐波那契数列", Homework.commonTest, {
                'prompt': "请输入数字: ",
                'call': lambda s: print("%s ==> %d, %d" %
                                    (s, Homework.fbFor(int(s)),
                                        Homework.fbRec(int(s))))
                })
        m.add("猴子吃桃", Homework.commonTest, {
                'prompt': "请输入天数: ",
                'call': lambda s: print("==> %d" % Homework.peach(int(s)))
                })
        m.add("括号匹配", Homework.commonTest, {
                'prompt': "请输入一行字符串: ",
                'call': lambda s: print(Homework.match(s))
                })
        m.add("逆古兰表达式", Homework.commonTest, {
                'prompt': "请输入表达式: ",
                'call': lambda s: print("s = ", Homework.expression(s))
                })
        m.add("(5 _ 3) _ 2 = 4")
        m.add("迷宫求解")
        m.add("退出")
        self.m = m

    def __call__(self):
        return self.m.run()

    @staticmethod
    def reTest(call, prompt="请输入: "):
        """
        重复测试使用
        """
        while True:
            usrInput = input(prompt)
            if usrInput == 'q' or call(usrInput):
                break


    @staticmethod
    def commonTest(i, args):
        """
        菜单项通用回调处理函数
        """
        Homework.reTest(args['call'], args['prompt'])


    @staticmethod
    def outNum(num, bit=16, end='\n'):
        """
        十进制转其它进制算法
        """
        def _outNum(num, bit):
            if num == 0:
                return ''
            return _outNum(num // bit, bit) + '0123456789ABCDEF'[num % bit]

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


    @staticmethod
    def outNumTest(usrInput):
        """
        十进制转其它进制: 断除法
        """
        try:
            print(Homework.outNum(*[int(x) for x in usrInput.split()]))
        except:
            pass


    @staticmethod
    def fbFor(n):
        """
        斐波那契数列循环实现
        """
        n1 = n2 = 1

        for i in range(2, n + 1):
            n1, n2 = n2, n1 + n2

        return n1

    @staticmethod
    def fbRec(n):
        """
        斐波那契数列递归实现
        """
        if n <= 2:
            return 1
        return Homework.fbRec(n - 1) + Homework.fbRec(n - 2)



    @staticmethod
    def peach(day):
        """
        猴子吃桃, 每天吃前一天一半多一个, 第五天吃完剩一个, 求没吃之前桃的个数(94)
        """
        if day == 0:
            return 1
        return 2 * (Homework.peach(day - 1) + 1)


    @staticmethod
    def match(s):
        """
        括号匹配算法
        """
        stack = []

        for r in s:
            if r in '{([':
                stack.append(r)
            elif r in ']})':
                if not stack:
                    return "缺少左括号"
                l = stack.pop()
                if (r == ']' and l != '['
                    or r == ')' and l != '('
                    or r == '}' and l != '{'):
                    return "左右不匹配"

        if stack:
            return "缺少右括号"

        return s


    @staticmethod
    def expression(s):
        """
        逆古兰表达式算法
        """
        stack = [int(c) for c in s if '0' <= c <= '9'][::-1]
        op = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b,
                '%': lambda a, b: a % b,
                '^': lambda a, b: a ** b
             }

        try:
            for c in s:
                if c in '+-*/%^':
                    stack.append(op[c](stack.pop(), stack.pop()))
            if len(stack) != 1:
                raise Exception
        except:
            return None

        return stack.pop()


    def mazeTest(i, args):
        pass

    def equal4Test(i, args):
        pass

if __name__ == "__main__":
    Homework()()

