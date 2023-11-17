import socket 
import threading

"""
Connect to server socket
Handle mssages from user

2 threads
1 to listen for messages from server
1 to gather input from user
"""

host = '127.0.0.1'
port = 55553
username = input("Type in a username: ")

def write(client):
    while True:
        message = input(">")
        client.send(message.encode("utf-8"))

def receive(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "USERNAME":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connected to server!")

    writeThread = threading.Thread(target=write, args=(client,))
    writeThread.start()
    receiveThread = threading.Thread(target=receive, args=(client,))
    receiveThread.start()

