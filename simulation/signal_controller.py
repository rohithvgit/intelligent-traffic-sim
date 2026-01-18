from scheduler.signal_scheduler import SignalScheduler
from config import BASE_GREEN_TIME


class SignalController:
    def __init__(self, intersection):
        self.intersection = intersection
        self.scheduler = SignalScheduler()

        # Assumption: average discharge rate
        # 1 car every 2 seconds → 0.5 cars/sec
        self.cars_per_second = 0.5

    def run_cycle(self):
        # 1. Select road using priority queue
        selected_road = self.scheduler.select_road(
            self.intersection.get_roads()
        )

        # 2. Green signal duration (time-based)
        green_duration = BASE_GREEN_TIME  # seconds

        # 3. Compute throughput
        max_passable = int(green_duration * self.cars_per_second)
        actual_cleared = min(
            max_passable,
            selected_road.vehicle_count()
        )

        # 4. Clear vehicles
        for _ in range(actual_cleared):
            selected_road.queue.popleft()

        # 5. Update starvation counters
        for road in self.intersection.get_roads():
            if road != selected_road:
                road.red_cycles += 1
            else:
                road.red_cycles = 0

        return selected_road, actual_cleared
