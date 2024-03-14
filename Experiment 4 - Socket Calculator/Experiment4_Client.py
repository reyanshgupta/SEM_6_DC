from socket import *

def client():
    serverip = input("Enter server's IP: ")
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((serverip, 12345))

    while True:
        response = client_socket.recv(1024).decode()
        print(response)
        message = input() 
        client_socket.send(message.encode())
        if message == '5':
            break

    client_socket.close()

if __name__ == "__main__":
    client()
