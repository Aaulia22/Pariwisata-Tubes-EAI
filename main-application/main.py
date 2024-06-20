import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# URL layanan yang terhubung ke jaringan docker internal
TICKET_BOOKING_URL = "http://ticket-booking-service:3000/bookings"
TOURIST_INFO_URL = "http://tourist-info-service:5000/info"

@app.route('/check-bookings', methods=['GET'])
def check_bookings():
    response = requests.get(TICKET_BOOKING_URL)
    return jsonify(response.json())

@app.route('/check-info', methods=['GET'])
def check_info():
    response = requests.get(TOURIST_INFO_URL)
    return jsonify(response.json())

@app.route('/bookings', methods=['GET', 'POST'])
def bookings():
    if request.method == 'GET':
        response = requests.get(TICKET_BOOKING_URL)
        return jsonify(response.json())
    elif request.method == 'POST':
        app.logger.info(f"POST /bookings request data: {request.json}")
        response = requests.post(TICKET_BOOKING_URL, json=request.json)
        app.logger.info(f"POST /bookings response: {response.json()}")
        return jsonify(response.json())

@app.route('/bookings/<int:id>', methods=['PUT', 'DELETE'])
def modify_booking(id):
    url = f"{TICKET_BOOKING_URL}/{id}"
    if request.method == 'PUT':
        app.logger.info(f"PUT /bookings/{id} request data: {request.json}")
        response = requests.put(url, json=request.json)
        app.logger.info(f"PUT /bookings/{id} response: {response.json()}")
        return jsonify(response.json())
    elif request.method == 'DELETE':
        app.logger.info(f"DELETE /bookings/{id}")
        response = requests.delete(url)
        app.logger.info(f"DELETE /bookings/{id} response: {response.json()}")
        return jsonify(response.json())

@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'GET':
        response = requests.get(TOURIST_INFO_URL)
        return jsonify(response.json())
    elif request.method == 'POST':
        app.logger.info(f"POST /info request data: {request.json}")
        response = requests.post(TOURIST_INFO_URL, json=request.json)
        app.logger.info(f"POST /info response: {response.json()}")
        return jsonify(response.json())

@app.route('/info/<int:id>', methods=['PUT', 'DELETE'])
def modify_info(id):
    url = f"{TOURIST_INFO_URL}/{id}"
    if request.method == 'PUT':
        app.logger.info(f"PUT /info/{id} request data: {request.json}")
        response = requests.put(url, json=request.json)
        app.logger.info(f"PUT /info/{id} response: {response.json()}")
        return jsonify(response.json())
    elif request.method == 'DELETE':
        app.logger.info(f"DELETE /info/{id}")
        response = requests.delete(url)
        app.logger.info(f"DELETE /info/{id} response: {response.json()}")
        return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
