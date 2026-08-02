# 📈 Real-Time Stock Market Streaming Pipeline

A real-time stock market dashboard built using Apache Kafka, Flask, Python, HTML, CSS, and JavaScript.

## 🚀 Features

- Real-time stock price streaming
- Apache Kafka Producer & Consumer
- Flask REST API
- Live dashboard updates every 2 seconds
- Responsive UI
- Event-driven architecture

---

## 🛠️ Tech Stack

- Python
- Apache Kafka
- Flask
- HTML5
- CSS3
- JavaScript
- REST API

---

## 📂 Project Structure

```
stock-market-streaming-pipeline
│
├── producer.py
├── consumer.py
├── app.py
├── requirements.txt
├── README.md
│
├── static
│   ├── style.css
│   └── app.js
│
├── templates
│   └── index.html
│
└── data
```

---

## ⚙️ Architecture

```
Producer
     │
     ▼
Kafka Topic (stock-prices)
     │
     ▼
Kafka Consumer
     │
     ▼
Flask API
     │
     ▼
Live Dashboard
```

---

## ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start Kafka

```bash
brew services start kafka
```

Run Producer

```bash
python producer.py
```

Run Dashboard

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

## 📸 Screenshot

_Add a screenshot of the dashboard here after pushing to GitHub._

---

## 📌 Future Improvements

- Live Yahoo Finance API integration
- AWS S3 storage
- AWS Glue
- Amazon Athena
- Docker support
- Power BI dashboard
- Deployment to AWS