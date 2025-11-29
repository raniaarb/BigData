from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'iot-machines',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Listening for IoT Data...")

for msg in consumer:
    data = msg.value
    print("Received:", data)

    # تحليل الأعطال
    if data["temperature"] > 80:
        print("🔥 ALERT: High temperature on machine", data["machine_id"])

    if data["vibration"] > 4.0:
        print("⚠️ ALERT: High vibration on machine", data["machine_id"])
