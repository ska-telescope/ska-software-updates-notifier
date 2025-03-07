"""SUN HTTP Server that serves prometheus metrics about APT packages
"""
import threading

from apt_pkg import Error  # pylint: disable=no-name-in-module
from flask import Flask, Response

from config import config
from prometheus import generate_metrics
from updates import get_apt_updates

app = Flask(__name__)
updates = {}


# Periodically update the cache
def update_cache():
    """Self-scheduling function for updating the APT cache"""
    # pylint: disable=global-statement
    global updates
    try:
        updates = get_apt_updates(config)
    except Error:
        pass
    # Schedule the update in 1 hour
    timer = threading.Timer(int(config["packages"]["delay"]), update_cache)
    timer.daemon = True
    timer.start()


# Force initial update
update_cache()


# Server the metrics on the /metrics endpoint
@app.route("/metrics")
def metrics():
    """Generates the Prometheus metrics"""
    return Response(generate_metrics(config, updates), mimetype="text/plain")


# Start the HTTP server
if __name__ == "__main__":
    from waitress import serve

    print(f"Listening on port {config['metrics']['port']}...")
    serve(app, host="0.0.0.0", port=int(config["metrics"]["port"]))
