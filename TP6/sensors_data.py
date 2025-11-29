import random
import time

def generate_sensor_data():
    return {
        "machine_id": random.randint(1, 5),
        "temperature": round(random.uniform(20, 100), 2),
        "vibration": round(random.uniform(0.1, 5.0), 2),
        "pressure": round(random.uniform(1.0, 10.0), 2),
        "timestamp": time.time()
    }
