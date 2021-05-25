#!/usr/bin/env python3

from kyo.vtmenu import Menu
import os
import kyo.vt as vt
import sys

def show(itemObj, index, menuObj):
    def outfile(filename):
        if os.path.isdir(menuObj.root + "/" + filename):
            return menuObj.v.out(filename, vt.BLUE)
        return filename

    if index == menuObj.cur:
        print(menuObj.v.out(outfile(str(itemObj)), unline=True))
    else:
        print(outfile(str(itemObj)))

def subdir(i, m):
    filename = str(m.items[i])
    path = m.root + "/" + filename
    if os.path.isdir(path):
        lsdir(path)
    else:
        os.system("vim " + path)


def lsdir(root):
    v = Menu(hookOutItem=show, disNum=15, root=root, wait=False)
    for i in os.listdir(root):
        v.add(i, subdir, v)
    v.loop()


def main():
    lsdir(sys.argv[1] if len(sys.argv) > 1 else ".")

if __name__ == "__main__":
    main()
