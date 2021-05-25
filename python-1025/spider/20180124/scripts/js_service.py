import os
import socket

from selenium import webdriver

d = webdriver.Firefox()
d.implicitly_wait(10)
 
sock = socket.socket(socket.AF_INET)
sock.bind(('192.168.7.63', 8000))
sock.listen(5)

while True:
    client, addr = sock.accept()
    print('client %s connected' % str(addr))

    url = client.recv(1024).decode()

    print('start to perform url request')
    d.get(url)

    print('start sending page source back to client')
    client.send(d.page_source.encode())

    print('page source sent')
    client.close()
