
import xmlrpc.client

def main():
    with xmlrpc.client.ServerProxy("http://localhost:9000/") as proxy:
        binary_str = input("Enter a binary string to convert: ")
        result = proxy.binary_to_decimal(binary_str)
        print(f"The decimal representation is: {result}")

if __name__ == "__main__":
    main()
