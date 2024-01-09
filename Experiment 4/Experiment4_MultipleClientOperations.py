from socket import *
import threading
import random
import time

def client_simulation(client_id):
    serverip = "127.0.0.1"  # Replace with your server's IP if different
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((serverip, 12345))

    try:
        # Simulating a sequence of operations
        for _ in range(3):  # Each client will perform 3 operations
            time.sleep(random.randint(1, 3))  # Random delay to simulate real-time behavior

            # Random operation and numbers
            operation = str(random.randint(1, 4))
            num1 = str(random.randint(1, 100))
            num2 = str(random.randint(1, 100))

            # Logging the data being sent
            print(f"Client {client_id} - Sending Operation: {operation}, Num1: {num1}, Num2: {num2}")

            # Sending data to server
            client_socket.send(operation.encode())
            server_response = client_socket.recv(1024).decode()  # Acknowledgement for operation
            print(f"Client {client_id} - Server response: {server_response}")

            client_socket.send(num1.encode())
            server_response = client_socket.recv(1024).decode()  # Acknowledgement for num1
            print(f"Client {client_id} - Server response: {server_response}")

            client_socket.send(num2.encode())
            server_response = client_socket.recv(1024).decode()  # Result from server
            print(f"Client {client_id} - Server response: {server_response}")

        # Sending quit signal
        client_socket.send('5'.encode())

    except Exception as e:
        print(f"Client {client_id} Exception: {e}")

    finally:
        client_socket.close()
        print(f"Client {client_id} has disconnected.")

if __name__ == "__main__":
    client_threads = []

    # Starting 5 client simulations
    for i in range(5):
        thread = threading.Thread(target=client_simulation, args=(i+1,))
        client_threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in client_threads:
        thread.join()
