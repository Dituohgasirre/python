#!/usr/bin/env python3


import os
import sys
from pwd import getpwnam
from getpass import getpass
from crypt import crypt
from spwd import getspnam


#  注意:
    #  此程序必须使用sudo运行
    #  观察进程树来实现此作业: pstree -p | grep bash

#  pwd.getpwnam
#  spwd.getspnam
#  getpass.getpass
#  crypt.crypt
#  os.getuid
#  os.setuid
#  os.setgid
#  os.setgroups
#  os.chdir
#  os.environ
#  os.fork
#  os.execl
#  os.wait


if __name__ == "__main__":
    def main():
        user = 'root' if len(sys.argv) < 2 else sys.argv[1]
        info = getpwnam(user)

        spwd = getspnam(user)
        pwd = crypt(getpass("密码: "), spwd.sp_pwdp)
        if pwd != spwd.sp_pwdp:
            print("密码验证失败!")
            return

        if not os.fork():
            os.environ['HOME'] = info.pw_dir
            os.chdir(info.pw_dir)
            os.initgroups(user, info.pw_gid)
            os.setgid(info.pw_gid)
            os.setuid(info.pw_uid)
            os.execl("/bin/bash", "/bin/bash")
        os.wait()

    main()
