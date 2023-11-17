import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
clients = []

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            for username, c in clients:
                if c != client:
                    c.send(message)
        except Exception as e:
            for c in clients:
                if client == c:
                    clients.remove(c)
            break
    client.close()
    print("disconnect!")
            

def main():
    PORT = 1234
    server.bind(("127.0.0.1", PORT))    
    server.listen()
    print(f"Server is listening at {PORT}")
    while True:
        client, addr = server.accept()
        username = client.recv(1024)
        print(f"{username.decode()} has been added to the chat!")
        clients.append((username.decode(), client))
        ht = threading.Thread(target=handle, args=(client,))
        ht.start()

if __name__ == "__main__":
    main()