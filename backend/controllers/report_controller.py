from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from controllers.utils import role_required
from services.report_service import admin_reports

report_bp = Blueprint("reports", __name__, url_prefix="/admin")

@report_bp.route("/reports", methods=["GET"])
@jwt_required()
@role_required("admin")
def reports():
    data = admin_reports()

    return jsonify([
        {
            "user": r.user,
            "book": r.book,
            "borrow_date": r.borrow_date,
            "return_date": r.return_date,
            "delay_days": r.delay_days or 0,
            "amount": float(r.amount) if r.amount else 0
        }
        for r in data
    ])
