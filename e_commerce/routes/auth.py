from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from e_commerce.models import db, User

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()
    if user and data.get("password") == user.password:
        login_user(user)
        return jsonify({"message": "Logged in successfully"}), 200
    return jsonify({"message": "Unauthorized. Invalid credentials"}), 401

@auth.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successfully"}), 200
