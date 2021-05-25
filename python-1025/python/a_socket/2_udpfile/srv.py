#!/usr/bin/env python3


import socket
import os
import sys
import glob
from net import Packet
from multiprocessing import *

"""
客户端:
    1. 给服务器发送请求(文件名 验证信息)  Packet.CONN
    2. 等待服务器回应包
        等到Packet.Error错误包打印错误信息退出程序
        等到Packet.CONN_ACK包程序继续
    3. 打开接受数据的文件
    4.
        while True:
            等待服务器的数据包      Packet.DATA
            将数据写入文件
            给服务器回应数据接受包  Packet.DATA_ACK

服务器:
    服务器处理客户端请求流程:
        1. 创建处理客户端请求的专用套接字

        2. 收到客户端请求
            验证用户信息, 验证不通过回应错误包      Packet.Error
            验证文件是否存在并且可读, 文件不存在或不可读回应错误包  Packet.Error
            验证通过则回应验证通过包                Packet.CONN_ACK

        3. 打开操作的文件
        4.
            while True:
                读取文件部分内容
                将读取数据发送客户端
                等待客户端数据接受回应包

    for i in range(5):
        创建进程并且处理客户端请求
"""

def client_handle(data, addr, packet):
    try:
        f = open("/tmp/" + data['data'], "rb")
        while True:
            fileData = f.read(512)
            if not fileData:
                break
            packet.send(fileData, addr, Packet.DATA)
            packet.recv(Packet.ACK)
        packet.send('', addr, Packet.QUIT)
        f.close()
    except Exception as e:
        packet.send(str(e), addr, Packet.ERROR)


def client_connect(packet):
    while True:
        try:
            data = packet.recv(Packet.CONN)
        except Exception as e:
            return print(e)
        data, addr = data
        print("client connect: ", addr, ", data: ", data)
        packet.sd = socket.socket(type=socket.SOCK_DGRAM)
        client_handle(data, addr, packet)
        print("client handle end: ", addr)
        #  packet.sd.close()


if __name__ == "__main__":
    def main():
        sd = socket.socket(type=socket.SOCK_DGRAM)
        sd.bind(('0.0.0.0', 9000))
        packet = Packet(sd)

        os.setpgrp()

        p = Pool(5)

        for i in range(5):
            p.apply_async(client_connect, args=(packet, ))

        filename = "/tmp/kyosrv.%d" % os.getpid()
        with open(filename, "w") as f:
            pass

        p.close()
        p.join()

        sd.close()

    def isRun():
        g = glob.glob("/tmp/kyosrv.*")
        if not g:
            return False
        return int(g[0].split('.')[1])


    pid = isRun()
    if len(sys.argv) < 2:
        if not pid and not os.fork():
            main()
    else:
        if sys.argv[1] == 'stop':
            if not pid:
                print("服务没有运行....")
            else:
                os.kill(-pid, 9)
                os.unlink('/tmp/kyosrv.%d' % pid)

