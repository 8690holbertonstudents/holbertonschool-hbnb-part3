from flask import Blueprint, jsonify, request
from models.users import User
from persistence.datamanager import DataManager
from validate_email_address import validate_email

user_api = Blueprint("user_api", __name__)
datamanager = DataManager(flag=1)

@user_api.route("/users", methods=["POST"])
def add_user():
    """
    Function used to create a new user, send it to the database datamanager
    and read a list of existing users.
    """
    if request.method == "POST":
        user_data = request.get_json()
        if not user_data:
            return jsonify({"Error": "Problem during user creation."}), 400

        email = user_data.get("email")
        first_name = user_data.get("first_name")
        last_name = user_data.get("last_name")
        if not all([email, first_name, last_name]):
            return jsonify({"Error": "Missing required field."}), 400
        if not all(c.isascii() for c in first_name) or not first_name.isalpha():
            return jsonify({"Error": "First name must contain only ascii characters."}), 400
        if not all(c.isascii() for c in last_name) or not first_name.isalpha():
            return jsonify({"Error": "Last name must contain only ascii characters."}), 400

        is_email_valid = validate_email(email)
        if not is_email_valid:
            return jsonify({"Error": "Email not valid"}), 400
        try:
            is_email_uniq = User.query.filter_by(email=User.email).all()
            if is_email_uniq:
                return jsonify({"Error": "User already exists"}), 409
        except FileNotFoundError:
            pass

        new_user = User(email=email, first_name=first_name, last_name=last_name)
        if not new_user:
            return jsonify({"Error": "setting up new user"}), 500
        else:
            datamanager.save(new_user)
            return jsonify({"Success": "User added"}), 201
