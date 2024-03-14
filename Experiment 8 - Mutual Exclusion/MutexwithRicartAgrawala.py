import threading
import queue
import time
import random

class Process(threading.Thread):
    def __init__(self, pid, timestamp, processes):
        threading.Thread.__init__(self)
        self.pid = pid
        self.timestamp = timestamp
        self.processes = processes
        self.queue = queue.Queue()
        self.acknowledged = 0

    def run(self):
        # Simulate process work before entering critical section
        work_time = random.random()
        print(f"Process {self.pid} doing pre-critical work for {work_time:.2f} seconds.")
        time.sleep(work_time)

        # Requesting to enter critical section
        print(f"Process {self.pid} requesting to enter critical section.")
        self.request_critical_section()

        # Wait for acknowledgment from all processes
        while self.acknowledged < len(self.processes) - 1:
            time.sleep(0.01)

        # Critical section
        print(f"Process {self.pid} is in critical section.")
        time.sleep(0.1)  # Simulate work in critical section
        print(f"Process {self.pid} is leaving critical section.")

        # Exiting critical section
        self.exit_critical_section()

    def request_critical_section(self):
        self.timestamp = time.time()
        self.acknowledged = 0
        for p in self.processes:
            if p.pid != self.pid:
                p.queue.put(('request', self.timestamp, self.pid))
                print(f"Process {self.pid} sent request to Process {p.pid}.")

    def exit_critical_section(self):
        print(f"Process {self.pid} exited critical section and is now sending release messages.")
        for p in self.processes:
            if p.pid != self.pid:
                p.queue.put(('release', self.timestamp, self.pid))

    def process_messages(self):
        while not self.queue.empty():
            msg, timestamp, pid = self.queue.get()
            if msg == 'request':
                print(f"Process {self.pid} received request from Process {pid}.")
                if (self.timestamp, self.pid) > (timestamp, pid) or self.timestamp == 0:
                    print(f"Process {self.pid} sending ack to Process {pid} because it has higher priority or is not interested.")
                    self.processes[pid].queue.put(('ack', self.timestamp, self.pid))
                else:
                    print(f"Process {self.pid} deferring ack to Process {pid}.")
                    self.queue.put(('deferred', timestamp, pid))
            elif msg == 'release':
                print(f"Process {self.pid} received release from Process {pid}, processing deferred requests if any.")
                while not self.queue.empty():
                    deferred_msg = self.queue.get()
                    if deferred_msg[0] == 'deferred':
                        _, deferred_timestamp, deferred_pid = deferred_msg
                        self.processes[deferred_pid].queue.put(('ack', self.timestamp, self.pid))
                        print(f"Process {self.pid} sent deferred ack to Process {deferred_pid}.")
            elif msg == 'ack':
                self.acknowledged += 1
                print(f"Process {self.pid} received ack from Process {pid}.")

def main():
    num_processes = 5
    processes = [Process(pid, time.time(), []) for pid in range(num_processes)]

    for p in processes:
        p.processes = processes

    for p in processes:
        p.start()

    while True:
        alive = False
        for p in processes:
            p.process_messages()
            alive = alive or p.is_alive()
        if not alive:
            break

if __name__ == '__main__':
    main()
