from flask_jwt_extended import verify_jwt_in_request, get_jwt, get_jwt_identity
from functools import wraps
from flask import jsonify

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()

            claims = get_jwt()
            if claims.get("role") != role:
                return jsonify({"error": "Yetkisiz"}), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper
