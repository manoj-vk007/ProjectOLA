from fastapi import FastAPI
import sqlite3

app = FastAPI()

DB = "data/ev.db"


@app.get("/")
def home():
    return {"message": "EV Fleet Health API Running"}


@app.get("/vehicles")
def get_vehicles():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT *
        FROM telemetry
        ORDER BY rowid DESC
        LIMIT 100
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]


@app.get("/vehicle/{vehicle_id}")
def get_vehicle(vehicle_id: int):

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    row = conn.execute("""
        SELECT *
        FROM telemetry
        WHERE vehicle_id=?
        ORDER BY rowid DESC
        LIMIT 1
    """, (vehicle_id,)).fetchone()

    conn.close()

    if row:
        return dict(row)

    return {"error": "Vehicle not found"}


@app.get("/alerts")
def alerts():

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT *
        FROM telemetry
        WHERE soh < 75
        ORDER BY rowid DESC
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]