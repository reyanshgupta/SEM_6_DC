class LamportClock:
    def __init__(self):
        self.clock = 0

    def tick(self):
        self.clock += 1
        return self.clock

    def send_message(self):
        self.tick() 
        return {"timestamp": self.clock}

    def receive_message(self, message):
        received_timestamp = message["timestamp"]
        self.clock = max(self.clock, received_timestamp) + 1

    def event_occurs(self):
        return self.tick()

    def get_time(self):
        return self.clock


# Example usage
if __name__ == "__main__":
    process_a = LamportClock()
    process_b = LamportClock()
    process_a.event_occurs()
    message = process_a.send_message() 
    process_b.receive_message(message) 
    process_b.event_occurs()
    print(f"Process A's clock: {process_a.get_time()}")
    print(f"Process B's clock: {process_b.get_time()}")
