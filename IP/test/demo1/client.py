import socket
import sys

IP="192.168.41.11"
port=40005

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((IP,port))
except Exception as e:
    print("server not found")
    sys.exit()

while True:
    trigger=input("send")
    s.sendall(trigger.encode())
    data=s.recv(1024)
    data.decode()
    print("recevied:",data)
    if trigger.lower()=='1':
        break

s.close()
