
class Process:
    def __init__(self, id):
        self.id = id
        self.clock = 0
    def send_message(self, receiver):
        self.clock += 1
        print(f"Process {self.id} sends message with clock {self.clock} to Process {receiver.id}")
        receiver.receive_message(self.clock)

    def receive_message(self, sender_clock):
        self.clock = max(self.clock, sender_clock) + 1
        print(f"Process {self.id} receives message and updates clock to {self.clock}")

P1 = Process('P1')
P2 = Process('P2')
P3 = Process('P3')

P1.send_message(P2)  
P2.send_message(P3) 
P3.send_message(P1)  
P1.send_message(P2)  
