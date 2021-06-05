#!/usr/bin/env python3


import socket
from pargs import parse
from net import Packet


if __name__ == "__main__":
    def main():
        args, opt = parse(['s|srv|1', 'p|port|1'])
        srvIp = opt['srv'] if 'srv' in opt else "3.3.3.3"
        port = int(opt['port']) if 'port' in opt else 9000

        sd = socket.socket(type=socket.SOCK_DGRAM)
        addr = (srvIp, port)
        packet = Packet(sd)

        while True:
            cmd = input("<自己的网络SHELL>: ")
            packet.send(cmd, addr, Packet.DATA)
            if cmd == "exit":
                break
            out = ""
            while True:
                data, addr = packet.recv()
                if data['type'] == Packet.QUIT:
                    break
                out += data['data']
            print(out)

        sd.close()

    main()
