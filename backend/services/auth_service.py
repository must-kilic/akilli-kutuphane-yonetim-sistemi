from flask_jwt_extended import create_access_token
from entities.user import User

def login(email, password):
    user = User.query.filter_by(email=email, password=password).first()
    if not user:
        return None

    token = create_access_token(
        identity=str(user.id),              
        additional_claims={
            "role": user.role,
            "email": user.email
        }
    )

    return token
