import tkinter as tk

class TrafficVisualizer:
    def __init__(self, intersection):
        self.intersection = intersection
        self.root = tk.Tk()
        self.root.title("Intelligent Traffic Signal - Visual Mode")
        self.root.geometry("600x600")
        self.root.configure(bg="#2c3e50") # Dark background for contrast

        # Canvas for drawing the intersection
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="#2c3e50", highlightthickness=0)
        self.canvas.pack()

        # Coordinates for the 4-way intersection (Cross shape)
        self.center_x, self.center_y = 300, 300
        self.road_width = 120
        self.lane_length = 250
        
        # Initial draw
        self.update(None)

    def _draw_road_layout(self):
        # Draw vertical road (A & C)
        self.canvas.create_rectangle(
            self.center_x - self.road_width/2, 0,
            self.center_x + self.road_width/2, 600,
            fill="#34495e", outline=""
        )
        # Draw horizontal road (B & D)
        self.canvas.create_rectangle(
            0, self.center_y - self.road_width/2,
            600, self.center_y + self.road_width/2,
            fill="#34495e", outline=""
        )
        
        # Draw dashed lane markers
        self.canvas.create_line(self.center_x, 0, self.center_x, 600, fill="white", dash=(20, 20))
        self.canvas.create_line(0, self.center_y, 600, self.center_y, fill="white", dash=(20, 20))
        
        # Clear center intersection area (optional aesthetic)
        self.canvas.create_rectangle(
            self.center_x - self.road_width/2, self.center_y - self.road_width/2,
            self.center_x + self.road_width/2, self.center_y + self.road_width/2,
            fill="#5D6D7E", outline=""
        )

    def _draw_signal(self, x, y, color, label):
        # Draw the traffic light body
        self.canvas.create_rectangle(x-20, y-20, x+20, y+20, fill="black")
        # Draw the light
        self.canvas.create_oval(x-15, y-15, x+15, y+15, fill=color, outline="white")
        # Draw label (Road ID)
        self.canvas.create_text(x, y-35, text=f"Road {label}", fill="white", font=("Arial", 12, "bold"))

    def _draw_cars(self, road_id, count):
        # Define start positions and directions for cars based on Road ID
        # Assume: A=North, B=East, C=South, D=West (Incoming traffic)
        
        car_size = 20
        gap = 5
        
        # Starting positions for the queue (at the stop line)
        positions = {
            "A": (self.center_x - self.road_width/4, self.center_y - self.road_width/2 - 10, 0, -1), # X, Y, dx, dy (dy is -1 to stack upwards)
            "B": (self.center_x + self.road_width/2 + 10, self.center_y - self.road_width/4, 1, 0),
            "C": (self.center_x + self.road_width/4, self.center_y + self.road_width/2 + 10, 0, 1),
            "D": (self.center_x - self.road_width/2 - 10, self.center_y + self.road_width/4, -1, 0)
        }

        if road_id not in positions: return

        start_x, start_y, dx, dy = positions[road_id]

        for i in range(count):
            # Calculate position for the i-th car in queue
            cx = start_x + (dx * (i * (car_size + gap)))
            cy = start_y + (dy * (i * (car_size + gap)))
            
            # Draw car
            self.canvas.create_rectangle(
                cx - car_size/2, cy - car_size/2,
                cx + car_size/2, cy + car_size/2,
                fill="#e74c3c", outline="black"
            )

    def update(self, green_road_id):
        self.canvas.delete("all")
        self._draw_road_layout()

        # Coordinates for signals (near the corners of the intersection)
        # Top-Left (A), Top-Right (B), Bottom-Right (C), Bottom-Left (D) - mapped to incoming lanes
        signal_positions = {
            "A": (self.center_x - 40, self.center_y - 80),
            "B": (self.center_x + 80, self.center_y - 40),
            "C": (self.center_x + 40, self.center_y + 80),
            "D": (self.center_x - 80, self.center_y + 40)
        }

        for road_id, road in self.intersection.roads.items():
            # Determine color
            color = "green" if road_id == green_road_id else "red"
            
            # Draw Signal
            if road_id in signal_positions:
                sx, sy = signal_positions[road_id]
                self._draw_signal(sx, sy, color, road_id)
            
            # Draw Cars
            self._draw_cars(road_id, road.vehicle_count())

        # Draw Status Text
        status_text = f"GREEN SIGNAL: Road {green_road_id}" if green_road_id else "Initializing..."
        self.canvas.create_text(
            300, 550, 
            text=status_text, 
            fill="#2ecc71", 
            font=("Courier", 16, "bold")
        )

        self.root.update()