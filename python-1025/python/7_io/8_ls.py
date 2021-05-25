#!/usr/bin/env python3

import os
import sys
from time import strftime, localtime
from pwd import getpwuid
from grp import getgrgid
from stat import *

#  特权位/粘贴位(s S t T)
#  软链接
#  对齐排版
#  大小加单位(K M G T) ls -h
#  颜色(文件类型 权限(x 特权位) 后缀名)


class Ls:
    def __init__(self, args):
        filename = args[1]
        o = os.lstat(filename)
        p = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
        t = " pc d b - l s"[S_IFMT(o.st_mode) >> 12]
        t += p[(o.st_mode & S_IRWXU) >> 6]
        t += p[(o.st_mode & S_IRWXG) >> 3]
        t += p[o.st_mode & S_IRWXO]

        print(t, o.st_nlink,
                getpwuid(o.st_uid).pw_name,
                getgrgid(o.st_gid).gr_name,
                o.st_size,
                strftime("%F %H:%M", localtime(o.st_mtime)),
                filename)


if __name__ == "__main__":
    c = Ls(sys.argv)
