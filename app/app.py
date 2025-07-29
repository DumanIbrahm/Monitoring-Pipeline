from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
import logging

app = Flask(__name__)

# Logging ayarı
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Prometheus metrikleri
REQUEST_COUNT = Counter('app_request_count', 'Toplam istek sayısı', ['endpoint'])

@app.route('/')
def home():
    REQUEST_COUNT.labels(endpoint='/').inc()
    app.logger.info('Ana sayfa görüntülendi.')
    return 'Hello, DevOps!'

@app.route('/health')
def health():
    REQUEST_COUNT.labels(endpoint='/health').inc()
    app.logger.info('Health endpoint çağrıldı.')
    return jsonify(status='UP'), 200

@app.route('/error')
def error():
    REQUEST_COUNT.labels(endpoint='/error').inc()
    app.logger.error('Simüle hata oluştu.')
    return jsonify(error='Simulated error'), 500

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
