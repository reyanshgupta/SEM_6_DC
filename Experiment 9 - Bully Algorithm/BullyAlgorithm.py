class BullyAlgorithm:
    def __init__(self, process_id, num_processes):
        self.process_id = process_id
        self.num_processes = num_processes
        self.coordinator = None
        self.processes = [True] * num_processes

    def start_election(self):
        print(f"Process {self.process_id} starts election.")
        higher_processes = [i for i in range(self.process_id + 1, self.num_processes)]
        for i in higher_processes:
            if self.processes[i]:
                print(f"Process {self.process_id} sends election message to process {i}.")
                self.receive_election(self.process_id, i)

        # If no higher process responds, this process becomes coordinator
        if not any(self.processes[i] for i in higher_processes):
            self.coordinator = self.process_id
            print(f"Process {self.process_id} has elected itself as coordinator.")

    def receive_election(self, sender_id, receiver_id):
        print(f"Process {receiver_id} receives election message from process {sender_id}.")

        if self.process_id > receiver_id:
            print(f"Process {receiver_id} sends OK message to process {sender_id}.")
            self.receive_ok(receiver_id, sender_id)

    def receive_ok(self, sender_id, receiver_id):
        print(f"Process {receiver_id} receives OK message from process {sender_id}.")
        self.coordinator = sender_id

    def run(self):
        self.start_election()

        while self.coordinator is None:
            pass

        print(f"Process {self.process_id} has elected process {self.coordinator} as coordinator.")

# Example usage
num_processes = 5
process_id = 2

algorithm = BullyAlgorithm(process_id, num_processes)
algorithm.run()
