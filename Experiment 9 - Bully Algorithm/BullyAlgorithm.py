class Process:
    def __init__(self, pid):
        self.pid = pid  
        self.active = True  
    def __str__(self):
        return f"Process {self.pid}"

    def start_election(self, processes):
        print(f"{self} starts an election.")
        answers = []
        for p in processes:
            if p.pid > self.pid:
                print(f"{self} sends election message to {p}")
                if p.active:
                    answers.append(p.receive_election(self, processes))
        if not answers:
            self.announce_victory(processes)
        else:
            print(f"{self} received answers from others, stepping down.")

    def receive_election(self, initiator, processes):
        if self.active:
            print(f"{self} responds to {initiator}'s election message.")
            self.start_election(processes)
            return True
        return False

    def announce_victory(self, processes):
        for p in processes:
            if p.pid != self.pid:
                print(f"{self} sends victory message to {p}")
        print(f"{self} is the new coordinator.\n")

def simulate_bully_algorithm(process_ids):
    processes = [Process(pid) for pid in process_ids]
    processes[1].start_election(processes)  

    #Simulating failure
    processes[3].active = False
    print("After deactivating a process:\n")
    processes[2].start_election(processes)

if __name__ == "__main__":
    process_ids = [1, 2, 3, 4, 5]  
    simulate_bully_algorithm(process_ids)