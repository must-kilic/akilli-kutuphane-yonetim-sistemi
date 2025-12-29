from database import db
from entities.borrow import Borrow
from entities.user import User
from entities.book import Book
from entities.penalty import Penalty

def get_admin_reports():
    return db.session.query(
        Borrow.id.label("borrow_id"),
        User.email.label("user"),
        Book.title.label("book"),
        Borrow.borrow_date,
        Borrow.return_date,
        Penalty.delay_days,
        Penalty.amount
    ) \
    .join(User, User.id == Borrow.user_id) \
    .join(Book, Book.id == Borrow.book_id) \
    .outerjoin(Penalty, Penalty.borrow_id == Borrow.id) \
    .order_by(Borrow.borrow_date.desc()) \
    .all()
