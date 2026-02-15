from flask import Flask, jsonify
import logging
from app.config import Config


app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

)

)

@app.route("/")
def root():
    logging.info("Root endpoint accessed")
    return jsonify({
        "service": "Enterprise DevOps Platform",
        "status": "Active"
    })

@app.route("/health")
def health():
    return jsonify({"health": "OK"})

@app.route("/metrics")
def metrics():
    return jsonify({"uptime": "Running"})

@app.route("/cloud")
def cloud():
    logging.info(f"Cloud endpoint accessed - Provider: {Config.CLOUD_PROVIDER}")
    return jsonify({
        "cloud": Config.CLOUD_PROVIDER,
        "environment": Config.ENVIRONMENT
    })

    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
