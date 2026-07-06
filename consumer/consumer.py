from kafka import KafkaConsumer
import json
import joblib
import sqlite3

# Load trained model
model = joblib.load("models/model.pkl")

# SQLite
conn = sqlite3.connect("data/ev.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS telemetry (
    vehicle_id INTEGER,
    temperature REAL,
    soc REAL,
    voltage REAL,
    speed REAL,
    soh REAL
)
""")
conn.commit()

# Kafka Consumer
consumer = KafkaConsumer(
    "telemetry",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="latest"
)

print("Listening for telemetry...\n")

for msg in consumer:

    data = msg.value

    features = [[
        data["temperature"],
        data["soc"],
        data["voltage"],
        data["speed"]
    ]]

    soh = float(model.predict(features)[0])

    cursor.execute("""
        INSERT INTO telemetry
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["vehicle_id"],
        data["temperature"],
        data["soc"],
        data["voltage"],
        data["speed"],
        soh
    ))

    conn.commit()

    print({
        **data,
        "predicted_soh": round(soh,2)
    })