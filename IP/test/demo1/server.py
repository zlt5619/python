import socket
from tkinter import messagebox

IP="192.168.41.11"
port=40005
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((IP,port))
s.listen(1)

conn,addr=s.accept()
messagebox.showinfo(title="服务器窗口",message=addr)

while True:
    data=conn.recv(1024)
    data.decode()
    if not data:
        break
    messagebox.showinfo(title="服务器窗口",message=data)
    send=input('return')
    conn.sendall(send.encode())

conn.close()
s.close()
