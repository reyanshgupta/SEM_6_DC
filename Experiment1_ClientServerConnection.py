from socket import *
import threading
import time

def server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    client_socket.send(f"Client Address: {address} \n".encode())
    client_socket.send("I am the server!".encode())
    client_socket.close()
    server_socket.close()

def client():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
    message = client_socket.recv(1024).decode()
    print(f"Client: {message}")
    client_socket.close()

server_thread = threading.Thread(target=server)
client_thread = threading.Thread(target=client)

server_thread.start()
time.sleep(2)
client_thread.start()

server_thread.join()
client_thread.join()