"""
*****Server*****
Create a socket 
bind to a host/port 
listen on that socket

Accept new connections
When a new connection comes in
start a new thread for that client which is a long running process

receive and listen


"""
import socket
import threading

host = '127.0.0.1'
port = 55553
usernames = []
clients = []
user_info = {}

# handle messages from clients
def handle(client, username):
    while True:
        try:
            message = client.recv(1024)
            broadcast(username, message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = username[index]
            broadcast(username, "{username} left the chat!".encode("utf-8"))
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        client.send("USERNAME".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")
        user_info[username] = client
        usernames.append(username)
        clients.append(client)

        print(f"Username is {username}")
        broadcast(username, f"{username} joined the chat!".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client, username))
        thread.start()

def broadcast(username, message):
    for _username, client in user_info.items():
        if _username != username:
            client.send(username.encode("utf-8") + "> ".encode("utf-8") + message)

if __name__ == "__main__":
    # Starting Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    receive()