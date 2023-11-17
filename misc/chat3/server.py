import socket 
import threading
import sys
"""
Start a thread that handles incoming messages
"""

HOST, PORT = "127.0.0.1", 1237
FORMAT = "utf-8"

clients = {}

def broadcast(client: socket.socket, message):
    for username, other_client in clients.items():
        if client == other_client:
            continue
        other_client.send(message.encode(FORMAT))
    
def handleIncoming(client: socket.socket):
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if not message:
                break
            broadcast(client, message)
        except: 
            n = ""
            for nickname, c in clients.items():
                if client == c:
                    n = nickname 
            del clients[client]
            broadcast(client, f"{n} has disconnected from the chat")
    client.close()
def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(10)
    print(f"Server is listening!")

    while True:
        client, address = serverSocket.accept()
        # Request And Store Nickname
        client.send('USERNAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients[nickname] = client
        broadcast(client, f"{nickname} has joined the chat!")
        thread = threading.Thread(target=handleIncoming, args=(client,))
        thread.start()

if __name__ == "__main__":
    sys.exit(main())

