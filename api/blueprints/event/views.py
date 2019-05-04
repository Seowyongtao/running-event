from flask import Blueprint, request, jsonify
from models.event import Event
from models.user import User
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

  
    name= request.json.get('name', None)
    file_name = request.json.get('file_name', None)
    category = request.json.get('category', None)
    location = request.json.get('location', None)
    reward = request.json.get('reward', None)
    event_date = request.json.get('event_date', None)
    registration_closes = request.json.get('registration_closes', None)
    description = request.json.get('description', None)
    registration_fee = request.json.get('registration_fee', None)

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
    if not registration_fee:
        errors.append('registration_fee')
    if not description:
        errors.append('description')
    if errors:
        return jsonify({"msg":{"Missing Parameters":[error for error in errors]}}), 400
    
    event = Event(name= name,file_name= file_name,category =category, location=location, reward=reward, 
                  event_date=event_date, registration_closes=registration_closes, description=description, registration_fee=registration_fee, user_id=id)

    event.save()


   

    return jsonify({
        "message": "Successfully create a new event",
        "status": "success"
    }), 200


@event_api_blueprint.route('/show', methods=['GET'])
@jwt_required
def show_event():
     
    events = Event.select()

    return jsonify({
        "status": "success",
        "event": [{
            "event_id":event.id,
            "name":event.name,
            "file_name":event.file_name,
            "category":event.category,
            "location":event.location,
            "reward":event.reward,
            "event_date":event.event_date,
            "registration_fee":event.registration_fee,
            "registration_closes":event.registration_closes,
            "description":event.description
        } for event in events]
    }), 200

@event_api_blueprint.route('/show/<id>', methods=['GET'])
@jwt_required
def show_myevent(id):
     
    events = Event.select().where(Event.user_id==id)

    return jsonify({
        "status": "success",
        "event": [{
            "event_id":event.id,
            "name":event.name,
            "file_name":event.file_name,
            "category":event.category,
            "location":event.location,
            "reward":event.reward,
            "event_date":event.event_date,
            "registration_fee":event.registration_fee,
            "registration_closes":event.registration_closes,
            "description":event.description
        } for event in events]
    }), 200