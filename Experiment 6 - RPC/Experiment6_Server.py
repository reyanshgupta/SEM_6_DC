from xmlrpc.server import SimpleXMLRPCServer
import logging

logging.basicConfig(level=logging.INFO)

class BinaryConverter:
    def binary_to_decimal(self, binary_str):
        try:
            return int(binary_str, 2)
        except ValueError:
            return "Error: Invalid binary string."

def main():
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
    logging.info("Listening on port 9000...")
    server.register_instance(BinaryConverter())
    server.serve_forever()

if __name__ == '__main__':
    main()
