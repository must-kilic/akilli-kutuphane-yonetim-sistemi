from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.borrow_service import BorrowingService

borrowing_bp = Blueprint(
    "borrowings",
    __name__,
    url_prefix="/api/borrowings"
)

@borrowing_bp.route("/", methods=["POST"])
@jwt_required()
def borrow():
    user_id = int(get_jwt_identity())
    BorrowingService.borrow_book(user_id, request.json)
    return {"message": "Book borrowed"}

@borrowing_bp.route("/return/<int:borrowing_id>", methods=["PUT"])
@jwt_required()
def return_book(borrowing_id):
    BorrowingService.return_book(borrowing_id)
    return {"message": "Book returned"}

@borrowing_bp.route("/", methods=["GET"])
@jwt_required()
def list_borrowings():
    user_id = int(get_jwt_identity())
    return {"borrowings": BorrowingService.list_borrowings(user_id)}
