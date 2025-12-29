from database import db

class Penalty(db.Model):
    __tablename__ = "penalty"

    id = db.Column(db.Integer, primary_key=True)
    borrow_id = db.Column(db.Integer, nullable=False)
    delay_days = db.Column(db.Integer)
    amount = db.Column(db.Numeric(10, 2))
