import socket
import threading


USERNAME = input("What is your username > ")
def receive(client):
    while True:
        message = client.recv(1024).decode("utf-8")
        if message == "USERNAME":
            print("received username")
            client.send("USERNAME".encode("utf-8"))
            client.recv(1024)
            client.send(USERNAME.encode("utf-8"))            
            

def write():
    while True:
        user_input = input(">")

def main():
    ADDR = ("127.0.0.1", 1234)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    receiveThread = threading.Thread(target=receive, args=(client,))
    receiveThread.start()
    # writeThread = threading.Thread(target=write, args=(client,))
    # writeThread.start()
    
if __name__ == "__main__":
    main()