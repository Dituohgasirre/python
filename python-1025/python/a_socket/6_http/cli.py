#!/usr/bin/env python3


import socket
import http.client as hc
import urllib.request
import requests


if __name__ == "__main__":
    def socket_http():
        sd = socket.socket()
        #  sd.connect(('14.215.177.38', 80))
        #  sd.send("GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n".encode())
        sd.connect(('3.3.3.3', 80))
        sd.send("GET /python/6_function/1_args.py\r\n\r\n".encode())

        while True:
            data = sd.recv(1024)
            if not data:
                break
            print(data.decode())

        sd.close()

    def httpclient():
        conn = hc.HTTPConnection("3.3.3.3")
        conn.request('GET', '/python/6_function/1_args.py')
        r = conn.getresponse()
        print(r.read().decode())

    def urllibTest():
        with urllib.request.urlopen("http://3.3.3.3/python/6_function/1_args.py") as f:
            print(f.read().decode())

    def requestsTest():
        r = requests.get("http://3.3.3.3/python/6_function/1_args.py")
        print(r.text)

    #  socket_http()
    #  httpclient()
    #  urllibTest()
    requestsTest()
