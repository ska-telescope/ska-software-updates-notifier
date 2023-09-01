from config import config
from updates import get_apt_updates
from prometheus import generate_metrics
from flask import Flask
import threading

app = Flask(__name__)
updates = {}

# Periodically update the cache
def update_cache():
    global updates
    updates = get_apt_updates(config)
    t = threading.Timer(3600, update_cache)
    t.daemon = True
    t.start()

# Force initial update
update_cache()

# Server the metrics on the /metrics endpoint
@app.route('/metrics')
def metrics():
    return generate_metrics(config, updates)

# Start the HTTP server
if __name__ == '__main__':
    from waitress import serve
    print(f"Listening on port {config['metrics']['port']}...")
    serve(app, host='0.0.0.0', port=config['metrics']['port'])
