from models.intersection import Intersection
from simulation.traffic_generator import generate_traffic
from simulation.signal_controller import SignalController
from gui.visualize import TrafficVisualizer


def main():
    intersection = Intersection("I1")
    controller = SignalController(intersection)
    gui = TrafficVisualizer(intersection)

    cycle_count = {"count": 0}  # mutable counter for closures

    def simulation_step():
        cycle_count["count"] += 1

        # 1. Generate traffic
        generate_traffic(intersection)

        # 2. Run scheduling cycle
        selected_road, cleared = controller.run_cycle()

        # 3. Update GUI
        gui.update(selected_road.road_id)

        # 4. Console output (clean & demo-friendly)
        print(
            f"Cycle {cycle_count['count']} | "
            f"Green: Road {selected_road.road_id} | "
            f"Cleared: {cleared}"
        )

        # 5. Schedule next cycle (non-blocking)
        gui.root.after(2000, simulation_step)

    # Start simulation after 1 second
    gui.root.after(1000, simulation_step)

    # Start GUI event loop
    gui.root.mainloop()


if __name__ == "__main__":
    main()
