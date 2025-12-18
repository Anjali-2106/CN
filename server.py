import socket
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5050))
server.listen(1)

print("----------- SERVER -----------")
print("SERVER is listening..")

conn, addr = server.accept()
print("Connection accepted from", addr)

# Send welcome message to client
conn.send("Hello there! msg from SERVER".encode())

while True:
    msg = conn.recv(1024).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"CLIENT [{timestamp}]: {msg}")

    if msg.lower() == "quit":
        break

    text = input("ENTER TEXT: ")
    conn.send(text.encode())

    if text.lower() == "quit":
        break

conn.close()
server.close()
