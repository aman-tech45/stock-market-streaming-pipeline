from flask import Flask, jsonify, render_template
from kafka import KafkaConsumer
import json
import threading

app = Flask(__name__)

latest_stock = {}

def consume_messages():
    consumer = KafkaConsumer(
        "stock-prices",
        bootstrap_servers="localhost:9092",
        auto_offset_reset="latest",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )

    for message in consumer:
        data = message.value
        latest_stock[data["symbol"]] = data


thread = threading.Thread(target=consume_messages)
thread.daemon = True
thread.start()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/stocks")
def stocks():
    return jsonify(latest_stock)


if __name__ == "__main__":
    app.run(debug=True)