from flask import Blueprint, jsonify, request
from models.users import User
from flask_jwt_extended import create_access_token
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
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    return 'Wrong username or password', 401
