from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db
from entities.book import Book
from controllers.utils import role_required

book_bp = Blueprint("book", __name__)

# 🔵 TÜM KULLANICILAR GÖREBİLİR
@book_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([
        {
            "id": b.id,
            "title": b.title,
            "author": b.author
        } for b in books
    ])

# 🔴 SADECE ADMIN EKLEYEBİLİR
@book_bp.route("/books", methods=["POST"])
@jwt_required()
@role_required("admin")
def add_book():
    data = request.json
    book = Book(
        title=data["title"],
        author=data["author"]
    )
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Kitap eklendi"})

# 🔴 SADECE ADMIN SİLER
@book_bp.route("/books/<int:id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Kitap bulunamadı"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Kitap silindi"})
