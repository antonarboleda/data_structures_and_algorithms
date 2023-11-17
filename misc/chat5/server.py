import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

clients = {}

def broadcast(message, client_socket):
    for username, other_socket in clients.items():
        other_socket.send(message)

def receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            broadcast(message.encode("utf-8"), client_socket)
        except Exception as e:
            for username, c_socket in clients.items():
                to_del = ""
                if c_socket == client_socket:
                    to_del = username
                del clients[to_del]
                print(f"{to_del} has left the chat")
            break

    
def main():
    print(f"Server is listening on port: {PORT}")
    while True:
        client_socket, address = server.accept()
        # Get user info because it's establishing a new conection
        client_socket.send("USERNAME".encode("utf-8"))
        username = client_socket.recv(1024).decode("utf-8")
        clients[username] = client_socket

        receive_thread = threading.Thread(target=receive, args=(client_socket,))
        receive_thread.start()


if __name__ == "__main__":
    main()