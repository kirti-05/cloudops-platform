from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "application": "CloudOps API",
            "version": "1.0.0",
            "environment": os.getenv("ENVIRONMENT", "local"),
            "message": "CloudOps API is running"
        }
    )


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "UP"
        }
    ), 200


@app.route("/ready")
def ready():
    return jsonify(
        {
            "status": "READY"
        }
    ), 200


@app.route("/api/v1/status")
def status():
    return jsonify(
        {
            "application": "CloudOps API",
            "status": "running"
        }
    ), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)