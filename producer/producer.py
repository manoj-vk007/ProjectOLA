from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)
print("Sending vehicle telemetry\n")
while True:
    data = {
        "vehicle_id": random.randint(1, 20),
        "temperature": round(random.uniform(25, 45), 2),
        "soc": random.randint(20, 100),
        "voltage": round(random.uniform(320, 420), 2),
        "speed": round(random.uniform(0, 120), 2)
    }
    producer.send("telemetry", data)
    producer.flush()
    print(data)
    time.sleep(1)