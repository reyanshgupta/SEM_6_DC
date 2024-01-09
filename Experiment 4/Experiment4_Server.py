from socket import *
import threading

lock = threading.Lock()

def server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5) 
    print("Server is listening for inputs...\n")
    
    while True:
        client_socket, address = server_socket.accept()
        with lock:
            print(f"Accepted connection from {address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

def handle_client(client_socket):
    try:
        while True:
            with lock:
                client_socket.send("Enter the operation number (1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Quit): ".encode())
            op = client_socket.recv(1024).decode()
            if op == '5':
                break
            with lock:
                client_socket.send("Enter the first number: ".encode())
            num1 = int(client_socket.recv(1024).decode())
            with lock:
                client_socket.send("Enter the second number: ".encode())
            num2 = int(client_socket.recv(1024).decode())

            result = calculator(int(op), num1, num2)
            with lock:
                client_socket.send(f"Result: {result}\n".encode())

    except Exception as e:
        with lock:
            print(f"Exception: {e}")
    finally:
        client_socket.close()

def calculator(operation, n1, n2):
    if operation == 1:
        return n1 + n2
    elif operation == 2:
        return n1 - n2
    elif operation == 3:
        return n1 * n2
    elif operation == 4:
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

if __name__ == "__main__":
    server()
