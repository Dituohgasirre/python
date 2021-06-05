#!/usr/bin/env python3


import socket
import sys
from pargs import parse


if __name__ == "__main__":
    def main():
        args, opt = parse(['s|srv|1', 'p|port|1'])
        srvIp = opt['srv'] if 'srv' in opt else '3.3.3.3'
        port = int(opt['port']) if 'port' in opt else 9000
        addr = (srvIp, port)

        sd = socket.socket(type=socket.SOCK_DGRAM)
        while True:
            data = input("发送: ")
            if data == "exit":
                break
            sd.sendto(data.encode(), addr)
            data, addr = sd.recvfrom(1024)
            data = data.decode()
            if data == "exit":
                break
            print(addr, "=", data)

        sd.close()

    main()
