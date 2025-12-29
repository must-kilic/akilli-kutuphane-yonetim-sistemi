from datetime import datetime
from entities.borrow import Borrow
from database import db
from repositories.borrow_repository import get_user_borrowings

class BorrowingService:

    @staticmethod
    def borrow_book(user_id, data):
        book_id = data.get("book_id")

        borrow = Borrow(
            user_id=user_id,
            book_id=book_id,
            borrow_date=datetime.utcnow()
        )

        db.session.add(borrow)
        db.session.commit()

    @staticmethod
    def return_book(borrowing_id):
        borrow = Borrow.query.get(borrowing_id)
        borrow.return_date = datetime.utcnow()
        db.session.commit()

    @staticmethod
    def list_borrowings(user_id):
        return get_user_borrowings(user_id)
