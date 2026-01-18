import heapq
from scheduler.priority_calc import calculate_priority


class SignalScheduler:
    def select_road(self, roads):
        heap = []

        for road in roads:
            priority = calculate_priority(road)
            # tie-breaker: road_id to avoid comparison of Road objects
            heapq.heappush(heap, (-priority, road.road_id, road))

        _, _, selected_road = heapq.heappop(heap)
        return selected_road
