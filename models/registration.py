from models.base_model import BaseModel
import peewee as pw
from models.user import User
from models.event import Event

class Registration(BaseModel):
    participant = pw.ForeignKeyField(User, backref="user")
    event = pw.ForeignKeyField(Event, backref="event")
    registration_fee=pw.CharField(null=True)
    first_name = pw.CharField(null=True)
    last_name = pw.CharField(null=True)
    email = pw.CharField(null=True)
    date_of_birth = pw.CharField(null=True)
    age = pw.CharField(null=True)
    gender = pw.CharField(null=True)
    nationality= pw.CharField(null=True)
    nric = pw.CharField(null=True)
    phone_number =pw.CharField(null=True)
    address =pw.CharField(null=True)
    