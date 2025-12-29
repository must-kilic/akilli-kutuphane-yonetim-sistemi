from entities.borrow import Borrow
from entities.book import Book
from database import db

def get_user_borrowings(user_id):
    return db.session.query(
        Borrow.id.label("borrow_id"),
        Book.title
    ).join(Book, Book.id == Borrow.book_id) \
     .filter(Borrow.user_id == user_id, Borrow.return_date == None) \
     .all()
