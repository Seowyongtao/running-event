from flask import Blueprint, request, jsonify, url_for
import os
from models.user import User
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity
)
from werkzeug.security import check_password_hash
from datetime import datetime,timedelta

login_api_blueprint = Blueprint('login_api',
                                __name__,
                                template_folder='templates')


@login_api_blueprint.route('/', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
   
    
    errors = []
    if not email:
        errors.append("email")
    if not password:
        errors.append("password")
    if errors:
        return jsonify({"msg": {"Missing parameters":[error for error in errors]}}), 400

    user = User.get_or_none(User.email == email)

    if user and check_password_hash(user.password, password):
        
        expires = timedelta(days=365)
        access_token = create_access_token(user.id, expires_delta=expires)


        return jsonify({
            "access_token": access_token,
            "message": "Successfully signed in.",
            "status": "success",
            "user": {
                "id": user.id,
                "username": user.username
            }
        }), 200
    else:
        return jsonify({"msg": "Bad login"}), 404
