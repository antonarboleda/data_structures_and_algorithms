import socket
import threading

username = input("What is your username?")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive():
    while True:
        try:
            message = client.recv(1024)
            if not message: 
                break
            print(message.decode())
        except Exception as e:
            print("An error has occcured!")            
            break
    client.close()

def write():
    while True:
        message = input("")
        client.send(f"{username} > {message}".encode())

if __name__ == "__main__":
    PORT = 1234
    client.connect(("127.0.0.1", PORT))
    client.send(username.encode())
    print("Connected!")
    rt = threading.Thread(target=receive)
    rt.start()
    wt = threading.Thread(target=write)
    wt.start()