from models.intersection import Intersection
from simulation.traffic_generator import generate_traffic
from simulation.signal_controller import SignalController

def main():
    intersection = Intersection("I1")
    controller = SignalController(intersection)

    for cycle in range(3):
        print(f"\n--- Cycle {cycle+1} ---")
        generate_traffic(intersection)

        road, cleared = controller.run_cycle()
        print(f"Green Signal: Road {road.road_id}")
        print(f"Vehicles cleared: {cleared}")

        for r in intersection.get_roads():
            print(f"Road {r.road_id}: {r.vehicle_count()} vehicles")

if __name__ == "__main__":
    main()
