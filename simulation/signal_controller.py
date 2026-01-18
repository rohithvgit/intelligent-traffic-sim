from scheduler.signal_scheduler import SignalScheduler

class SignalController:
    def __init__(self, intersection):
        self.intersection = intersection
        self.scheduler = SignalScheduler()

    def run_cycle(self):
        selected = self.scheduler.select_road(
            self.intersection.get_roads()
        )

        cleared = min(3, selected.vehicle_count())
        for _ in range(cleared):
            selected.queue.popleft()

        for road in self.intersection.get_roads():
            if road != selected:
                road.red_cycles += 1
            else:
                road.red_cycles = 0

        return selected, cleared
