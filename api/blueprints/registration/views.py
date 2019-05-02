from flask import Blueprint, request, jsonify
from models.event import Event
from models.user import User
from models.registration import Registration
from werkzeug.security import generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)

registration_api_blueprint = Blueprint('registration_api',
                             __name__,
                             template_folder='templates')


@registration_api_blueprint.route('/new', methods=['POST'])
@jwt_required
def new():

  
    event_id= request.json.get('event_id', None)
    registration_fee = request.json.get('registration_fee', None)
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    email= request.json.get('email', None)
    date_of_birth = request.json.get('date_of_birth', None)
    age = request.json.get('age', None)
    gender = request.json.get('gender', None)
    nationality = request.json.get('nationality', None)
    nric = request.json.get('nric', None)
    phone_number = request.json.get('phone_number', None)
    address = request.json.get('address', None)

    id = get_jwt_identity()
    user = User.get_or_none(User.id == id)
    

    

    errors=[]
    if not event_id:
        errors.append('event_id')
    if not registration_fee:
        errors.append('registration_fee')
    if not first_name:
        errors.append('first_name')
    if not last_name:
        errors.append('last_name')
    if not email:
        errors.append('email')
    if not date_of_birth:
        errors.append('date_of_birth')
    if not age:
        errors.append('age')
    if not gender:
        errors.append('gender')
    if not nationality:
        errors.append('nationality')
    if not nric:
        errors.append('nric')
    if not phone_number:
        errors.append('phone_number')
    if not address:
        errors.append('address')
    if errors:
        return jsonify({"msg":{"Missing Parameters":[error for error in errors]}}), 400
    
    registration = Registration(event_id=event_id, participant_id=user.id, registration_fee=registration_fee, first_name=first_name, last_name=last_name, email=email, address=address, date_of_birth=date_of_birth, age=age, gender=gender, nationality=nationality, nric=nric, phone_number=phone_number, address=address)

    registration.save()


   

    return jsonify({
        "message": "Successfully create a new event",
        "status": "success"
    }), 200