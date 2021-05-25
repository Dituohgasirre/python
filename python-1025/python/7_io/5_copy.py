#!/usr/bin/env python3

import sys
import os
from pargs import parse

#  1. 源为不存在路径 -
#  2. 目标为多级不存在路径 -
    #  直接报错

#  3. 源为存在的文件, 目标为不存在路径(路径最后一级不存在)
    #  直接复制

#  4. 源为存在的文件, 目标为存在文件路径
    #  根据-i / -u选项控制是否覆盖

#  5. 源为存在的文件, 目标为存在目录
    #  获取源文件名与目标目录组合路径, 并且回到第4种情况

#  6. 源为存在的目录, 目标为存在文件路径
    #  直接报错

#  7. 源为存在的目录, 目标为存在目录
    #  获取源目录名与目标目录组合路径

#  8. 源为存在的目录, 目标不存在路径(只限最后一级不存在)
    #  创建不存在路径并且复制目录(重命名)

#  9. 源为多个路径的情况 -

class CopyError(Exception):
    pass

class Copy:
    def __init__(self, args):
        args.pop(0)     #去除参数的程序名
        self.args, self.opt = parse(['r', 't|target|1', 'i', 'v', 'u'], args)
        src = dst = None
        if 'target' in self.opt:
            src = [os.path.realpath(x) for x in self.args]
            dst = os.path.realpath(self.opt['target'])
        else:
            *src, dst = [os.path.realpath(x) for x in self.args]

        for s in src:
            if not os.path.exists(s):
                raise CopyError("%s: 路径不存在!" % s)
            if os.path.isdir(s) and 'r' not in self.opt:
                raise CopyError("%s: 略过目录!" % s)

        if not os.path.exists(os.path.dirname(dst)):
            raise CopyError("%s: 目标路径多级不存在" % dst)

        print("src: ", src, ", dst: ", dst)
        #  print(self.args, self.opt)
        self.src, self.dst = src, dst

    def do(self):
        for src in self.src:
            if os.path.isdir(src):
                self.copydir(src, self.dst)
            else:
                self.copy(src, self.dst)

    def copydir(self, src, dst):
        if os.path.isfile(dst):
            raise CopyError("%s: 目标为存在文件" % dst)

        if os.path.isdir(dst):
            dst = dst + "/" + os.path.basename(src)

        os.makedirs(dst)

        for f in os.listdir(src):
            copypath = src + '/' + f
            dstpath = dst + '/' + f
            if os.path.isdir(copypath):
                self.copydir(copypath, dstpath)
            else:
                self.copy(copypath, dstpath)

    def copy(self, src, dst):
        while os.path.exists(dst):
            if os.path.isdir(dst):
                dst += '/' + os.path.basename(src)
            elif 'i' in self.opt:
                if input("是否覆盖(Y/N): ") not in 'yY':
                    return
                else:
                    break
            else:
                break

        if 'v' in self.opt:
            print("'%s' -> '%s'" % (src, dst))

        with open(src, "rb") as r:
            with open(dst, "wb") as w:
                w.write(r.read())

    def __call__(self):
        return self.do()

if __name__ == "__main__":
    Copy(sys.argv)()

