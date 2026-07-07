#  Ola Electric Vehicle Fleet Health & Range Anxiety Prevention

A real-time Electric Vehicle Fleet Monitoring and Predictive Analytics system built using Python, Kafka, FastAPI, PostgreSQL, Machine Learning, and Streamlit.

The system simulates telemetry data from electric delivery vehicles, detects battery degradation, predicts remaining driving range, identifies vehicles at risk of failure, and provides a real-time monitoring dashboard.


##  Project Overview

Electric vehicle fleets generate thousands of telemetry records every minute. Monitoring battery health manually is difficult and can lead to unexpected battery failures, reduced fleet efficiency, and range anxiety.

This project provides an end-to-end data engineering pipeline that:

- Simulates EV telemetry data
- Streams data using Apache Kafka
- Stores telemetry in PostgreSQL
- Detects battery degradation
- Predicts remaining driving range
- Generates battery health alerts
- Provides a real-time Streamlit dashboard
- Exposes APIs using FastAPI


#  Features

- Real-time EV telemetry simulation
- Kafka-based streaming architecture
- Battery State of Health (SoH) prediction
- Remaining range prediction using Machine Learning
- Battery degradation detection
- GPS tracking simulation
- Fleet monitoring dashboard
- REST APIs with FastAPI
- PostgreSQL data storage
- Docker support


#  Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| Streaming | Apache Kafka |
| Database | PostgreSQL |
| API | FastAPI |
| Dashboard | Streamlit |
| ML | Scikit-learn / XGBoost |
| Containerization | Docker |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |


#  Project Structure


ProjectOLA/
│
├── api/
├── consumer/
├── dashboard/
├── docker/
├── models/
├── producer/
├── database/
├── requirements.txt
├── docker-compose.yml
└── README.md


#  Installation

## 1. Install Git

Download and install Git.


## 2. Install Docker Desktop

Download Docker Desktop and ensure Docker Engine is running.


## 3. Install Python

Install Python 3.10 or above.



## 4. Clone Repository

bash
git clone https://github.com/manoj-vk007/ProjectOLA.git




## 5. Go to Project Directory

bash
cd mkv18



## 6. Create Virtual Environment

### Windows

bash
python -m venv .venv


Activate

bash
.venv\Scripts\activate


### Linux / Mac

bash
python3 -m venv .venv


bash
source .venv/bin/activate



## 7. Install Required Packages

bash
pip install -r requirements.txt



## 8. Start Docker Containers

bash
docker compose up




## 9. Generate Telemetry Data

 bash
python models/generate_data.py


## 10. Train Machine Learning Model

bash
python models/train_model.py

## 11. Start Kafka Producer

bash
python producer/producer.py


## 12. Start Kafka Consumer

bash
python consumer/consumer.py


## 13. Start FastAPI Server

bash
uvicorn api.app:app --reload


API Documentation

http://127.0.0.1:8000/docs



## 14. Start Streamlit Dashboard

bash
streamlit run dashboard/dashboard.py


Dashboard URL

http://localhost:8501


#  Project Workflow


Telemetry Generator
        │
        ▼
 Apache Kafka Producer
        │
        ▼
 Apache Kafka Broker
        │
        ▼
 Kafka Consumer
        │
        ▼
 PostgreSQL Database
        │
        ▼
Machine Learning Model
        │
        ▼
 FastAPI REST API
        │
        ▼
 Streamlit Dashboard


#  Expected Output

The system provides:

- Live vehicle telemetry
- Battery State of Health (SoH)
- Remaining range prediction
- Battery degradation alerts
- Fleet statistics
- GPS monitoring
- Charging recommendations
- Predictive maintenance alerts


# 🎯 Future Enhancements

- AWS Deployment
- Kubernetes Support
- Redis Caching
- Real GPS Integration
- Deep Learning Models
- Mobile Application
- Fleet Route Optimization

#  Author

**Manoj v Kulkarni**

M.Tech Data Engineering

GitHub

https://github.com/manoj-vk007

---

# 📜 License

This project is developed for educational and academic purposes.