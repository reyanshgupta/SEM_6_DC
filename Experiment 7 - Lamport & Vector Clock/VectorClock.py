class VectorClock:
    def __init__(self, nodes=None):
        self.clock = {node: 0 for node in nodes} if nodes else {}

    def update(self, node_id, timestamp=None):
        self.clock[node_id] = max(self.clock.get(node_id, 0), timestamp) if timestamp else self.clock.get(node_id, 0) + 1

    def merge(self, other):
        for node, timestamp in other.clock.items():
            self.clock[node] = max(self.clock.get(node, 0), timestamp)

    def __getitem__(self, node_id):
        return self.clock.get(node_id, 0)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.clock})"

if __name__ == "__main__":
    vc1 = VectorClock(['A', 'B', 'C'])
    vc2 = VectorClock(['A', 'B', 'C'])

    # Simulate events
    vc1.update('A') 
    vc1.update('A')  
    vc2.update('B') 
    print("VC1 before merge:", vc1)
    print("VC2 before merge:", vc2)
    # Node A's and B's events become known to each other
    vc1.merge(vc2)
    vc2.merge(vc1)
    print("VC1 after merge:", vc1)
    print("VC2 after merge:", vc2)
