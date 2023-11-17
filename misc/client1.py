import socket
import threading
PORT = 1200
state = {}
FORMAT = "utf-8"

def serverListen(serverSocket):
    while True:
        print("here!")
        msg = serverSocket.recv(1024).decode(FORMAT)
        if msg == "/messageSend":
            print("messageSend protocol received!")
            serverSocket.send(bytes(state["inputMessage"], "utf-8"))
            state["sendMessageLock"].release()
        else:
            print(msg)

def userInput(serverSocket):
    # state["sendMessageLock"].acquire()
    state["inputMessage"] = input()
    # state["sendMessageLock"].release()
    print("User input received!")
    if state["inputMessage"]:
        state["sendMessageLock"].acquire()
        serverSocket.send(b"/messageSend")

def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostbyname(socket.gethostname())
    serverSocket.connect((hostname, PORT))
    state["sendMessageLock"] = threading.Lock()

    threading.Thread(target=userInput, args=(serverSocket,)).start()
    threading.Thread(target=serverListen, args=(serverSocket,)).start()

if __name__ == "__main__":
    main()