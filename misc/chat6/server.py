import socket
import threading 
import sys

ADDR = ("127.0.0.1", 1234)
users = {}

def broadcast(sender_conn: socket.socket, message: bytes):
    for conn, user_info in users.items():
        conn.send(message)

def receive(client_conn):
    while True:
        message = client_conn.recv(1024).decode("utf-8")
        if not message:
            break
        elif message == "USERNAME":
            print("USERNAME!")
            client_conn.send("USERNAME".encode("utf-8"))
            username = client_conn.recv(1024)
            print(f"{username} is the username!, adding to users map")
            users[client_conn] = {"username": username}
        else:
            broadcast(client_conn, message.encode("utf-8"))
    del users[client_conn]
    client_conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    server.bind(ADDR)
    server.listen()
    print(f"Server listening on {ADDR}")
    while True:
        client_conn, client_addr = server.accept()
        client_conn.send("Connected to the chat server!".encode("utf-8"))
        client_conn.send("USERNAME".encode("utf-8"))
        receiver_thread = threading.Thread(target=receive, args=(client_conn,))
        receiver_thread.start()

if __name__ == "__main__":
    sys.exit(main())