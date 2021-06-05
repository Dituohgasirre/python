#!/usr/bin/env python3


import socket
from pargs import parse

if __name__ == "__main__":
    def main():
        args, opt = parse(['p|port|1'])
        port = int(opt['port']) if 'port' in opt else 9000

        sd = socket.socket(type=socket.SOCK_DGRAM)
        sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sd.bind(('0.0.0.0', port))

        while True:
            data, addr = sd.recvfrom(1024)
            data = data.decode()
            if data == "exit":
                break
            print(addr, "=", data)
            data = input("发送: ")
            if data == "exit":
                break
            sd.sendto(data.encode(), addr)

    main()
