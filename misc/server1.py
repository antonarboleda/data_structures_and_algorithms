import socket
import threading

PORT = 1200
FORMAT = "utf-8"
members = {}


def handleIncomingConn(client: socket.socket, addr):
    client_host, client_port = addr
    if not members.get((client_host, client_port), None):
        members[(client_host, client_port)] = client
    client.send(bytes("Welcome to the chat server!", FORMAT))
    print(f"Added {client_host}: {client_port} to chat!")
    while True:
        msg = client.recv(1024).decode(FORMAT)
        if msg == "/messageSend":
            print(f"Prepping message")
            client.send(bytes("/messageSend", FORMAT))
        else:
            print(f"Sending message!")
            for other_member in members.values():
                if other_member != client:
                    other_member.send(bytes(msg, FORMAT))

def main():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostbyname(socket.gethostname())
    listen_socket.bind((hostname, PORT))
    listen_socket.listen(10)
    print(f"Chat server running on {hostname}:{PORT}")
    while True:
        client, addr = listen_socket.accept()
        threading.Thread(target=handleIncomingConn, args=(client, addr)).start()

if __name__ == "__main__":
    main()