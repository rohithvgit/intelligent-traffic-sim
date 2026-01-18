import random
from models.vehicle import Vehicle
import time

def generate_traffic(intersection):
    for road in intersection.get_roads():
        arrivals = random.randint(0, 3)
        for _ in range(arrivals):
            vehicle = Vehicle(
                vehicle_id=f"V{random.randint(100,999)}",
                arrival_time=time.time()
            )
            road.add_vehicle(vehicle)
