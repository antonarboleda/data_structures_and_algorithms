import socket 
import threading
from typing import List
import select 
import time
IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

print("[SERVER START] Starting server")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen()

def handle_client_socket(client_socket: socket.socket, addr, client_sockets: List[socket.socket]):
    print(f"[CONNECTED] A new client {addr} has been connected")
    
    connected = True
    while connected:
        # msg = client_socket.recv(SIZE).decode(FORMAT)
        msg = "test"
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            print(f"[{addr}] {msg}")
            t = time.time()
            msg = str(time.time())
            print("here?")
            for neighbor_socket in client_sockets:
                    print(f"Sending to other socket: {neighbor_socket}")
                    neighbor_socket.send(msg.encode(FORMAT))
    client_socket.close()

def main():
    print(f"[CONNECTED] Listening on {IP}:{PORT}")
    reads = [server_socket]
    while True:
        read_sockets, write_sockets, err_sockets = select.select(reads, [], [])
        client_socket, addr = server_socket.accept()
        read_sockets.append(client_socket)
        # create a thread for the server to handle the client
        thread = threading.Thread(
            target=handle_client_socket, args=(client_socket, addr, read_sockets)
        )
        thread.start()
        print(f"Active connections: {threading.active_count()}")

if __name__ == "__main__":
    main()