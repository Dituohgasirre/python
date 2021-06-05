#!/usr/bin/env python3


import socket


if __name__ == "__main__":
    def main():
        sd = socket.socket()
        sd.connect(('3.3.3.3', 9000))

        while True:
            data = input("发送: ")
            sd.send(data.encode())
            data = sd.recv(1024).decode()
            if data.startswith("exit"):
                break
            print("data: ", data)

        sd.close()

    main()
