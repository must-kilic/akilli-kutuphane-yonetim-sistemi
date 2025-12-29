from flask import Blueprint, request, jsonify
from services.auth_service import login

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login_route():
    data = request.json
    token = login(data["email"], data["password"])
    if not token:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"token": token})
