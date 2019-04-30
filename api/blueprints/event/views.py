from flask import Blueprint, request, jsonify
from models.event import Event
from werkzeug.security import generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)

event_api_blueprint = Blueprint('event_api',
                             __name__,
                             template_folder='templates')


@event_api_blueprint.route('/new', methods=['POST'])
@jwt_required
def new():

     
    name= request.form.get('name', None)
    file_name = request.form.get('file_name', None)
    category = request.form.get('category', None)
    location = request.form.get('location', None)
    reward = request.form.get('reward', None)
    event_date = request.form.get('event_date', None)
    registration_closes = request.form.get('registration_closes', None)
    description = request.form.get('description', None)

    id = get_jwt_identity()

    errors=[]
    if not name:
        errors.append('name')
    if not file_name:
        errors.append('file_name')
    if not category:
        errors.append('category')
    if not location:
        errors.append('location')
    if not reward:
        errors.append('reward')
    if not event_date:
        errors.append('event_date')
    if not registration_closes:
        errors.append('registration_closes')
    if not description:
        errors.append('description')
    if errors:
        return jsonify({"msg":{"Missing Parameters":[error for error in errors]}}), 400
    
    event = Event(name= name,file_name= file_name,category =category, location=location, reward=reward, 
                  event_date=event_date, registration_closes=registration_closes, description=description)

    event.save()


   

    return jsonify({
        "message": "Successfully create a new event",
        "status": "success"
    }), 200