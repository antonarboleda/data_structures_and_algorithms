import socket

"""
Create a chat room
[ ] Allow multiple guests to connect
[ ] When a person enters the chat send to the others in the room
  "{IP} address had joined the room!"
[ ] Write the messages to disk so that when a new person joins the 
room they get the old messages. 
    - Bonus: Only get messages after a user has joined. They shouldn't see the
       the entire chat
[ ] - The server should be multithreaded
- Use netcat or telnet for stuff


"""
HEADER_SIZE = 8
import time
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5002))
    connect_requests_queue = 5
    server_socket.listen(connect_requests_queue)  
    while True:  
        clientsocket, address = server_socket.accept()
        msg = "Hi"
        msg = f"{len(msg)}#" + msg
        clientsocket.send(bytes(msg, "utf-8"))    
    
        while True:
            time.sleep(2)
            msg = f"The time is {time.time()}"
            msg = f"{len(msg)}#" + msg
            clientsocket.send(bytes(msg, "utf-8"))
    # while True:
    #     clientsocket, address = server_socket.accept()
    #     print(f"Got connection from {address}")
    #     msg = "Hi"
    #     msg = f"{len(msg):<{HEADER_SIZE}}" + msg
    #     clientsocket.send(bytes(msg, "utf-8"))
        # clientsocket.close()
if __name__ == "__main__":
    start_server()