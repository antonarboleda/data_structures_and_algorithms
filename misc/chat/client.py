import socket 
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    
    client.connect(ADDR)
    print(f"[CONNECTED] Connected to {IP}: {PORT}")

    connected = True
    while connected:
        # msg = input("> ")
        # client.send(msg.encode(FORMAT))
        # if msg == DISCONNECT_MSG:
        #     connected = False
        # else:
        msg = client.recv(SIZE).decode(FORMAT)            
        print(f"[SERVER] {msg}")
    client.close()

if __name__ == "__main__":
    main()