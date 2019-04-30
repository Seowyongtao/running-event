from models.base_model import BaseModel
import peewee as pw
from models.user import User

class Event(BaseModel):
    name=pw.CharField(null=True)
    file_name = pw.CharField(null=True)
    location = pw.CharField(null=True)
    category = pw.CharField(null=True)
    reward = pw.CharField(null=True)
    event_date = pw.CharField(null=True)
    registration_closes = pw.CharField(null=True)
    description = pw.CharField(null=True,max_length=255)
    user = pw.ForeignKeyField(User, backref="user")