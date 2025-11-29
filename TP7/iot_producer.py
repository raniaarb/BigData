from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Starting IoT Producer...")

while True:
    data = {
        "machine_id": random.randint(1, 5),
        "temperature": round(random.uniform(20, 100), 2),
        "vibration": round(random.uniform(0.1, 5.0), 2),
        "status": "RUNNING"
    }

    producer.send('iot-machines', data)
    print("Sent:", data)

    time.sleep(1)
