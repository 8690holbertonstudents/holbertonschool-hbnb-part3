from flask import Blueprint, jsonify, request
from models.users import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
login_api = Blueprint("login_api", __name__)


@login_api.route('/login', methods=['POST'])
def login():
    # Require data for login
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    # Query database for response
    user = User.query.filter_by(email=email).first()
    # Manage access token
    if user and User.check_password(user.password_hash, password):
        # Add role information to the token
        additional_claims = {"is_admin": user.is_admin}
        # Create user access token
        access_token = create_access_token(
            identity=user.id, additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    return jsonify({"Error": "Wrong access input"}), 401


def admin_only():
    claims = get_jwt()
    if claims.get("is_admin") is False:
        return False
    return True
