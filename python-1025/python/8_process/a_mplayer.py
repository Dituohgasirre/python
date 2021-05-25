#!/usr/bin/env python3


from kyo.vtmenu import Menu
import os
import time

def play(i, args):
    if not os.fork():
        os.dup2(args['mes'], 1)
        os.dup2(args['mes'], 2)
        os.execlp("mplayer", "mplayer", "./fa.wmv", "-quiet", "-slave",
                        "-input", "file=/tmp/fifo")
    time.sleep(1)
    os.read(args['mes'], 8192)
    get(i, {'cmd': "get_time_length", 'mes': args['mes']})

def ctl(i, args):
    ctlfile = open("/tmp/fifo", "w")
    print(ctlfile.write(args['cmd'] + '\n'))
    if args['cmd'] == 'q':
        return True

def get(i, args):
    ctl(i, args)
    print(os.read(args['mes'], 8192))

if __name__ == "__main__":
    def main():
        mes = os.open("/tmp/kyo", os.O_RDWR)
        m = Menu()
        m.add("播放", play, {'ctl': '/tmp/fifo', 'mes': mes})
        m.add("暂停", ctl, {'cmd': 'p'})
        m.add("快进", ctl, {'cmd':"seek 10"})
        m.add("快退", ctl, {'cmd':"seek -10"})
        m.add("获取", get, {'cmd':"get_time_pos", 'mes': mes})
        m.add("退出", ctl, {'cmd':"q"})
        m()

    main()
