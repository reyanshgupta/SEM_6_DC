from socket import *

def client():
    serverip = input("Enter server's IP: ")
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((serverip, 12345))

    while True:
        message = input("Enter a message to send to the server (or 'quit' to exit): ")
        if message.lower() == 'quit':
            break
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")

    client_socket.close()

if __name__ == "__main__":
    client()
