import os
import datetime
import jwt
from flask import Flask, jsonify, request

app = Flask(__name__)

SECRET_KEY = "innovacion_udea"

@app.route("/")
def hello_world():
    return f"Hello This is a test page"

@app.route("/get-token", methods=["POST"])
def get_token():
    data = request.get_json()
    user_id = data.get("user_id")
    role = data.get("role")

    if not user_id or not role:
        return jsonify({'error': 'user_id and role are required'}), 400

    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=10)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({'token': token})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)