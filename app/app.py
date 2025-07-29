from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import logging
from prometheus_client import Counter

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # → docker container içindeyken erişim için bind mount yapman gerekebilir
        logging.StreamHandler()
    ]
)


app = Flask(__name__)
metrics = PrometheusMetrics(app)
error_counter = Counter('flask_app_errors_total', 'Total number of errors in Flask app')
# Manual exception counter
from prometheus_client import Counter

@app.route("/")
def index():
    app.logger.info("Index endpoint hit")
    return jsonify({"message": "Welcome to the main page!"})

@app.route('/health')
def health():
    logging.info("Health check passed.")
    return jsonify({"status": "healthy"}), 200

@app.route('/error')
def error():
    logging.error("Error endpoint triggered!")
    error_counter.inc()  # ← Metric artışı
    raise Exception("Something went wrong!")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
