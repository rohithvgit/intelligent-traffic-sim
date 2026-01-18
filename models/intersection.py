from models.road import Road

class Intersection:
    def __init__(self, intersection_id, road_ids=None):
        self.intersection_id = intersection_id
        if road_ids is None:
            road_ids = ["A", "B", "C", "D"] # Default
            
        self.roads = { rid: Road(rid) for rid in road_ids }

    def get_roads(self):
        return self.roads.values()