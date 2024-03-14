import Pyro4

def query_binary_conversion():
    uri = input("Enter the URI of the server: ").strip()
    binary_converter = Pyro4.Proxy(uri)  
    
    binary_str = input("Enter a binary string to convert: ").strip()
    result = binary_converter.binary_to_decimal(binary_str)  
    print(f"The decimal representation is: {result}")

if __name__ == "__main__":
    query_binary_conversion()
