#!/usr/bin/env python3


import socket
from multiprocessing import Pool


def client_connect(sd):
    while True:
        cli, addr = sd.accept()
        print("client addr: ", addr)
        while True:
            data = cli.recv(1024)
            data = data.decode()
            print("%s|data(%d): " % (addr, len(data)), data)
            cli.send(("srv: " + data).encode())
            if data.startswith("exit"):
                break
        cli.close()

if __name__ == "__main__":
    def main():
        sd = socket.socket()
        sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sd.bind(('0.0.0.0', 9000))
        sd.listen(5)

        p = Pool(10)
        for i in range(10):
            p.apply_async(client_connect, args=(sd, ))

        p.close()
        p.join()

    main()
