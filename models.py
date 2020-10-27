# models.py
import flask_sqlalchemy
from app import db
from enum import Enum


class Kashusers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20))
    #messages = db.relationship('Kashmessenger', backref='sender')
    
    def __init__(self,b):
        self.user = b
        
    def __repr__(self):
        return '<Kashuser user : %s>' %self.user
        
        
class Kashmessenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120))
    #sender = db.Column(db.String(120))
    #sender= db.Column(db.String(120))
    #sender = db.Column(db.String(20), db.ForeignKey('kashusers.id'))

    def __init__(self, a): #add 'send' as an argument possibly
        self.message = a
        #self.sender = send

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