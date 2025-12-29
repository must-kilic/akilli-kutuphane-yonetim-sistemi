from flask import Blueprint, request, jsonify
from database import db
from entities.category import Category

category_bp = Blueprint("categories", __name__)

@category_bp.route("/categories", methods=["GET"])
def get_categories():
    return jsonify([{"id": c.id, "name": c.name} for c in Category.query.all()])

@category_bp.route("/categories", methods=["POST"])
def add_category():
    c = Category(name=request.json["name"])
    db.session.add(c)
    db.session.commit()
    return {"msg": "Added"}

@category_bp.route("/categories/<int:id>", methods=["DELETE"])
def delete_category(id):
    db.session.delete(Category.query.get(id))
    db.session.commit()
    return {"msg": "Deleted"}
