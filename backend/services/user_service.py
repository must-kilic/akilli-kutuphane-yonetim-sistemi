from repositories.user_repository import get_all_users, delete_user

def list_users():
    return get_all_users()

def remove_user(user_id):
    delete_user(user_id)
