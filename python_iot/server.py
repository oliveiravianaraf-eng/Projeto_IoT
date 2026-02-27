from flask import Flask, jsonify
from python_iot.main import setup, loop
import threading
import time

app = Flask(__name__)
ctx = setup()
latest_data = {}


def update_loop():
    global latest_data
    while True:
        latest_data = loop(ctx)
        time.sleep(5)


@app.route("/")
def index():
    return "<h1>IoT Sensor Data</h1><p>Visit <a href=\"/data\">/data</a> for JSON output.</p>"


@app.route("/data")
def data():
    return jsonify(latest_data)


if __name__ == "__main__":
    # start background update thread
    t = threading.Thread(target=update_loop, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=5000)
