#!/usr/bin/env python3


import socket
from net import Packet
from pargs import parse


if __name__ == "__main__":
    def main():
        args, opt = parse(['s|srv|1'])
        srvIp = opt['srv'] if 'srv' in opt else '3.3.3.3'
        filename = args[1]
        addr = (srvIp, 9000)

        sd = socket.socket(type=socket.SOCK_DGRAM)
        packet = Packet(sd)

        packet.send(filename, addr, Packet.CONN)
        f = open(filename, "wb")

        while True:
            data, addr = packet.recv()
            if data['type'] == Packet.ERROR:
                print("Error: ", data['data'])
                break
            elif data['type'] == Packet.QUIT:
                break
            elif data['type'] == Packet.DATA:
                f.write(data['data'])
                packet.send('', addr, Packet.ACK)


        f.close()
        sd.close()

    main()
