from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from time import sleep
from sqlalchemy import text

from config import Config
from database import db

from entities.user import User
from entities.book import Book
from entities.category import Category
from entities.borrow import Borrow
from entities.penalty import Penalty

from controllers.auth_controller import auth_bp
from controllers.book_controller import book_bp
from controllers.user_controller import user_bp
from controllers.borrowing_controller import borrowing_bp
from controllers.admin_controller import admin_bp
from controllers.report_controller import report_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)
JWTManager(app)

app.register_blueprint(admin_bp)
app.register_blueprint(report_bp)

app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)
app.register_blueprint(user_bp)
app.register_blueprint(borrowing_bp)
with app.app_context():
    sleep(3)  # postgres hazır olsun
    db.create_all()
    with db.engine.begin() as conn:
        conn.execute(text("""
        CREATE OR REPLACE FUNCTION calculate_penalty()
        RETURNS TRIGGER AS $$
        DECLARE
            allowed_days INTEGER := 14;
            late_days INTEGER;
            exists_penalty INTEGER;
        BEGIN
            IF NEW.return_date IS NOT NULL THEN
                SELECT COUNT(*) INTO exists_penalty
                FROM penalty
                WHERE borrow_id = NEW.id;

                IF exists_penalty = 0 THEN
                    late_days :=
                        EXTRACT(DAY FROM (NEW.return_date - NEW.borrow_date)) - allowed_days;

                    IF late_days > 0 THEN
                        INSERT INTO penalty (borrow_id, delay_days, amount)
                        VALUES (NEW.id, late_days, (late_days * 5)::NUMERIC);
                    END IF;
                END IF;
            END IF;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        """))

        conn.execute(text("""
        DROP TRIGGER IF EXISTS trg_calculate_penalty ON borrow;

        CREATE TRIGGER trg_calculate_penalty
        AFTER UPDATE OF return_date
        ON borrow
        FOR EACH ROW
        EXECUTE FUNCTION calculate_penalty();
        """))

        # STORED PROCEDURE
        conn.execute(text("""
        CREATE OR REPLACE PROCEDURE clear_user_penalties_by_email(p_email TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            DELETE FROM penalty
            WHERE borrow_id IN (
                SELECT b.id
                FROM borrow b
                JOIN "user" u ON u.id = b.user_id
                WHERE u.email = p_email
            );
        END;
        $$;
        """))
        
    # 🔵 SEED
    if not User.query.first():
        admin = User(
            email="admin@library.com",
            password="admin123",
            role="admin"
        )
        user = User(
            email="user@library.com",
            password="user123",
            role="user"
        )
        db.session.add_all([admin, user])
        db.session.commit()
        
from flask import send_from_directory

@app.route("/swagger")
def swagger():
    return send_from_directory("static", "swagger.json")

@app.route("/__routes__", methods=["GET"])
def list_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            "endpoint": rule.endpoint,
            "methods": list(rule.methods),
            "path": str(rule)
        })
    return routes

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
