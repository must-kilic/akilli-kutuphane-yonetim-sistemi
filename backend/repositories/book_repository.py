from database import db
from entities.book import Book
from entities.borrow import Borrow
from entities.user import User

def get_books_status():
    return db.session.query(
        Book.id,
        Book.title,
        Book.author,
        User.email.label("borrowed_by")
    ).outerjoin(Borrow, (Borrow.book_id == Book.id) & (Borrow.return_date == None)) \
     .outerjoin(User, User.id == Borrow.user_id) \
     .all()
