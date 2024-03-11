import Pyro4

@Pyro4.expose
class BinaryConverter(object):
    def binary_to_decimal(self, binary_str):
        try:
            decimal = int(binary_str, 2)
            return decimal
        except ValueError:
            return "Error: Invalid binary string."

def start_server():
    daemon = Pyro4.Daemon()                 
    uri = daemon.register(BinaryConverter)  
    
    print("Ready. Object uri =", uri)     
    daemon.requestLoop()             

if __name__ == "__main__":
    start_server()
