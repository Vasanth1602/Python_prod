from flask import Flask, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = Flask(__name__)

# Create a simple Counter metric
REQUEST_COUNTER = Counter('http_requests_total', 'Total HTTP requests received')

@app.route('/')
def home():
    REQUEST_COUNTER.inc()  # Increment the counter on each request
    return "Hello, Prometheus!"

# Prometheus metrics endpoint
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
