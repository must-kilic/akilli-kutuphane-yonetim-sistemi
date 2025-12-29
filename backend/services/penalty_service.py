from sqlalchemy import text
from database import db

def clear_penalties_by_email(email):
    with db.engine.begin() as conn:
        conn.execute(
            text("CALL clear_user_penalties_by_email(:email)"),
            {"email": email}
        )
