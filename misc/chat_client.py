import socket

HOST = "localhost"
PORT = 1234
HEADER_SIZE = 8

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    full_msg = ""
    new_msg = True
    while True:
        msg = s.recv(16)
        print("here")
        if new_msg:
            index = 0
            while msg[index] != "#":
                index += 1
                break
            new_msg
            # 2#hi
            # print(f"new msg length: {msg[:HEADER_SIZE]}")
            # print(msg[:HEADER_SIZE], "IS THE HEADERSIZE")
            msgLen = int(msg[:index])
            new_msg = False

        full_msg += msg.decode("utf-8")
        if len(full_msg) == msgLen:
            print("full msg recvd!")
            print(full_msg[HEADER_SIZE:])
            new_msg = True
            full_msg = ""
        print(full_msg)