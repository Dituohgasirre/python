#!/usr/bin/env python3


import sys
import os
import kyo.vt as vt
from pargs import parse


class GrepError(Exception):
    pass


class Grep:

    def __init__(self, args):
        args.pop(0)
        self.args, self.opt = parse(['b', 'r', 'n', '|color'], args)

        if len(self.args) < 2:
            raise GrepError("grep: 必须指定关键词和查找路径!")

        self.key, self.target = self.args

        if not os.path.exists(self.target):
            raise GrepError("grep: %s 没有那个文件和目录" % self.target)

        self.targetDir = False
        if os.path.isdir(self.target):
            self.targetDir = True
            if 'r' not in self.opt:
                raise GrepError("grep: %s 是一个目录, 请加 -r 选项"
                                 % self.target)

        if 'color' in self.opt:
            self.vt = vt.Vt()

        #  print(self.key, self.target, self.opt)

    def out(self, num, line, s=''):
        if 'color' in self.opt:
            m = self.vt.out(":", vt.CYAN)
            filepath = ""
            if self.targetDir:
                filepath = self.vt.out(s, vt.PURPLE) + m
        else:
            m = ":"
            filepath = s + m

        if 'n' in self.opt:
            if 'color' in self.opt:
                s = self.vt.out("%d" % num, vt.GREEN) + m
            else:
                s = "%d" % num

        s += line.rstrip('\n')
        if 'color' in self.opt:
            s = s.replace(self.key, self.vt.out(self.key, vt.RED, bold=True))

        print(filepath + s)

    def grep(self, target):
        try:
            f = open(target)

            for num, line in enumerate(f, 1):
                if self.key in line:
                    self.out(num, line, target)

        except UnicodeDecodeError:
            if 'b' in self.opt:
                print("%s 为二进制文件!" % target)
            return

        f.close()

    def grepdir(self, target):
        for f in os.listdir(target):
            t = os.path.realpath(target + '/' + f)
            if os.path.isdir(t):
                self.grepdir(t)
            else:
                self.grep(t)

    def do(self):
        if self.targetDir:
            self.grepdir(self.target)
        else:
            self.grep(self.target)


if __name__ == "__main__":
    try:
        g = Grep(sys.argv)
        g.do()
    except GrepError as e:
        print(e, file=sys.stderr)


