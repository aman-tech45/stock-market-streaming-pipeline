from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

stocks = ["AAPL", "TSLA", "GOOGL", "MSFT"]

print("🚀 Kafka Producer Started...\n")

while True:
    stock_data = {
        "symbol": random.choice(stocks),
        "price": round(random.uniform(100, 500), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send("stock-prices", stock_data)
    producer.flush()

    print(stock_data)

    time.sleep(2)