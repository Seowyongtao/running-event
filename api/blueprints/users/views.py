from flask import Blueprint, request, jsonify
from models.user import User
from werkzeug.security import generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['POST'])
def create():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    
    
    user_password = password
    hashed_password = generate_password_hash(user_password)

    errors=[]

    if not username:
        errors.append('username')
    if not password:
        errors.append('password')
    if not email:
        errors.append('email')
    if errors:
        return jsonify({"msg": {"Missing parameters": [error for error in errors]}}), 400
    
        
     # actual sign up users 
   

    # front_end side will do the validation
    # pattern_password = '\w{6,}'
    # result = re.search(pattern_password, user_password)
    # pattern_email = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]'
    # result_email = re.search(pattern_email,email)

    
    # duplicate username and email checking

    username_check = User.get_or_none(User.username == username)
    email_check = User.get_or_none(User.email == email)

    if not username_check and not email_check:

        u = User(username=username, email=email, password=generate_password_hash(password))

        u.save()
        user = User.get(User.username == username)
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "access_token": access_token,
            "message": "Successfully created a user and signed in.",
            "status": "success",
            "user": {
                "id": user.id,
                "username": user.username
            }
        }), 200
    else:
        return jsonify({"msg": "username or email already used"}), 400
