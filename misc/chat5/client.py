import socket
import threading

HOST = "127.0.0.1"
PORT = 1234
USERNAME = input("Please enter a username: ")

def write(client):
    while True:
        message = input(f"{USERNAME} > ")
        message = f"{USERNAME} > {message}"
        # logic to write messages
        client.send(message.encode("utf-8"))

def receive(client):
    while True:
        message = client.recv(1024).decode("utf-8")
        if message == "USERNAME":
            client.send(USERNAME.encode("utf-8"))
        else:
            print(message)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))    
    print("Welcome to the chat!")

    receive_thread = threading.Thread(target=receive, args=(client,))
    receive_thread.start()
    write_thread = threading.Thread(target=write, args=(client,))
    write_thread.start()

if __name__ == "__main__":
    main()
