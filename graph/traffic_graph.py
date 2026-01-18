class TrafficGraph:
    def __init__(self):
        self.graph = {}

    def add_intersection(self, intersection_id):
        self.graph[intersection_id] = []

    def connect(self, i1, i2):
        self.graph[i1].append(i2)
        self.graph[i2].append(i1)
