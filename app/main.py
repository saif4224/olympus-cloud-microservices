from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

# Simulate a Database of shipments
shipments = {
    "TRK123": {"status": "IN_TRANSIT", "location": "London Gateway", "delivery_date": "2026-02-05"},
    "TRK456": {"status": "DELIVERED", "location": "Manchester Depot", "delivery_date": "2026-01-20"},
    "TRK789": {"status": "PENDING", "location": "Warehouse", "delivery_date": "TBD"}
}

@app.route('/')
def health_check():
    # Show the Container ID (Hostname) to prove load balancing works later
    return jsonify({
        "service": "Olympus Logistics API",
        "status": "Healthy - V2 Updated",
        "container_id": socket.gethostname(),
        "timestamp": str(datetime.datetime.now())
    })

@app.route('/track/<tracking_id>')
def track_shipment(tracking_id):
    data = shipments.get(tracking_id)
    if data:
        return jsonify({"tracking_id": tracking_id, "data": data})
    else:
        return jsonify({"error": "Shipment not found"}), 404

if __name__ == '__main__':
    # Run on 0.0.0.0 to be accessible outside the container
    app.run(host='0.0.0.0', port=8080)

    