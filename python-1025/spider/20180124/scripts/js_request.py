import sys
import socket

host = '192.168.7.63'
port = 8000
url = sys.argv[1]
sock = socket.socket(socket.AF_INET)
sock.connect((host, port))
sock.send(url.encode())
html = sock.recv(409600).decode()
print(html, end='')
