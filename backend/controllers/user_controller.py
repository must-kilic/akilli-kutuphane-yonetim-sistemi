from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.borrow_service import BorrowingService
from database import db
from entities.penalty import Penalty

user_bp = Blueprint("users", __name__)

# ================================
# KULLANICININ ÖDÜNÇ ALDIĞI KİTAPLAR
# ================================
@user_bp.route("/my-borrowings", methods=["GET"])
@jwt_required()
def my_borrowings():
    user_id = int(get_jwt_identity())

    borrowings = BorrowingService.list_borrowings(user_id)

    return jsonify([
        {
            "borrow_id": b.borrow_id,
            "title": b.title
        }
        for b in borrowings
    ])


# ================================
# KULLANICININ CEZALARI
# ================================
@user_bp.route("/my-penalties", methods=["GET"])
@jwt_required()
def my_penalties():
    user_id = int(get_jwt_identity())

    from entities.borrow import Borrow

    penalties = (
        db.session.query(Penalty)
        .join(Borrow, Borrow.id == Penalty.borrow_id)
        .filter(Borrow.user_id == user_id)
        .all()
    )


    return jsonify([
        {
            "borrow_id": p.borrow_id,
            "delay_days": p.delay_days,
            "amount": float(p.amount)
        }
        for p in penalties
    ])
