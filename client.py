import socket
from datetime import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5050))


print("----------- CLIENT -----------")

# Receive welcome msg from server
msg = client.recv(1024).decode()
print(msg)

while True:
    text = input("ENTER TEXT: ")
    client.send(text.encode())

    if text.lower() == "quit":
        break

    msg = client.recv(1024).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"SERVER [{timestamp}]: {msg}")

    if msg.lower() == "quit":
        break

client.close()
