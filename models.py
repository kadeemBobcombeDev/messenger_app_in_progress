# models.py
import flask_sqlalchemy
from app import db
from enum import Enum


class Kashusers(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    user = db.Column(db.String(20))
    messages = db.relationship('Kashmessenger', backref='kashusers')
    
    def __init__(self,b,c):
        self.user = b
        self.id = c
        
    def __repr__(self):
        return '<Kashuser user : %s\nKashuser id : %s>' %(self.user, self.id)
        
        
class Kashmessenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120))
    sender = db.Column(db.String(20), db.ForeignKey('kashusers.id'))

    def __init__(self, a,sender): #add 'send' as an argument possibly
        self.message = a
        self.sender = sender

    def __repr__(self):
        return '<Kashmessenger message : %s>' % self.message 
        


class AuthUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auth_type = db.Column(db.String(120))
    name = db.Column(db.String(120))
    
    def __init__(self, name, auth_type):
        assert type(auth_type) is AuthUserType
        self.name = name
        self.auth_type = auth_type.value
        
    def __repr__(self):
        return "<User name: {}\ntype: {}".format(self.name, self.auth_type)
        

class AuthUserType(Enum):
    GOOGLE = "google"
    PASSWORD = "password"