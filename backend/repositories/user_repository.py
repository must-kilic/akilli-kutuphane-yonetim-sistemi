from entities.user import User
from database import db

def get_all_users():
    return User.query.all()

def delete_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
