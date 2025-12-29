from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controllers.utils import role_required
from services.book_service import books_status
from services.user_service import list_users, remove_user
from services.penalty_service import clear_penalties_by_email
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/books-status", methods=["GET"])
@jwt_required()
@role_required("admin")
def books_status_route():
    data = books_status()
    return jsonify([
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "borrowed_by": b.borrowed_by
        } for b in data
    ])

@admin_bp.route("/users", methods=["GET"])
@jwt_required()
@role_required("admin")
def users_route():
    users = list_users()
    return jsonify([
        {"id": u.id, "email": u.email, "role": u.role}
        for u in users
    ])

@admin_bp.route("/users/<int:id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_user_route(id):
    remove_user(id)
    return jsonify({"message": "User deleted"})

@admin_bp.route("/clear-penalties", methods=["POST"])
@jwt_required()
@role_required("admin")
def clear_penalties():
    data = request.get_json()
    email = data.get("email")

    if not email:
        return {"msg": "email gerekli"}, 400

    clear_penalties_by_email(email)
    return jsonify({"message": "Kullanıcının tüm cezaları silindi"})