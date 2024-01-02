from socket import *
import threading
import time

def server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5) 
    print("Server is listening...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

def handle_client(client_socket):
    try:
        client_socket.send(f"Welcome to the server!\n".encode())
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received from client: {message}")
            client_socket.send(f"Received: {message}".encode())
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server()
