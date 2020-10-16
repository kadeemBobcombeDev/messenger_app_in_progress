# models.py
import flask_sqlalchemy
from app import db


class kashmessenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120))
    
    def __init__(self, a):
        self.message = a
        
    def __repr__(self):
        return '<kashmessenger message : %s>' % self.message 
        

class kashusers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20))
    
    def __init__(self,b):
        self.user = b
        
    def __repr__(self):
        return '<kashuser user : %s>' %self.user
