import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 4949
s.bind((ip, port))

print("Listening for incoming connections...")
s.listen()

conn, addr = s.accept()

print("Connection received from: " + addr[0])

while True:
    command = input(">> ").encode()

    if command == b'exit':
        conn.send("exit".encode())
        conn.close()
        break
    
    conn.send(command)
    print(conn.recv(4096).decode())