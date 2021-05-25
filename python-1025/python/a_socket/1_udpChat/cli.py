#!/usr/bin/env python3


import socket
import sys
import os
from pargs import parse
from kyo.vtmenu import Menu


def choice(choiceList, title="请选择: "):
    def handle(i, args):
        args['return']['data'] = args['data']
        return True

    m = Menu(title=title)
    ret = {}
    for o in choiceList:
        m.add(str(o), handle, {'return': ret, 'data': o})
    m.loop()
    return ret['data']


if __name__ == "__main__":
    def main():
        args, opt = parse(['s|srv|1', 'p|port|1'])
        srvIp = opt['srv'] if 'srv' in opt else '3.3.3.255'
        port = int(opt['port']) if 'port' in opt else 9000
        addr = (srvIp, port)

        sd = socket.socket(type=socket.SOCK_DGRAM)
        sd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        print("sendto search server = ", sd.sendto("search".encode(), addr))
        sd.settimeout(1)
        srvlist = []
        try:
            while True:
                data, addr = sd.recvfrom(1024)
                print("聊天对象是: ", addr)
                srvlist.append(addr)
        except:
            if len(srvlist) == 0:
                print("没人理我....")
                os._exit(0)
        sd.settimeout(None)

        addr = choice(srvlist)
        print("选择的通信对象是: ", addr)
        while True:
            data = input("发送: ")
            print("sendto = ", sd.sendto(data.encode(), addr))
            if data == "exit":
                break

        sd.close()

    main()
