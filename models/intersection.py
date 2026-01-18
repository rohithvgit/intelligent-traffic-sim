from models.road import Road

class Intersection:
    def __init__(self, intersection_id):
        self.intersection_id = intersection_id
        self.roads = {
            "A": Road("A"),
            "B": Road("B"),
            "C": Road("C"),
            "D": Road("D")
        }

    def get_roads(self):
        return self.roads.values()
