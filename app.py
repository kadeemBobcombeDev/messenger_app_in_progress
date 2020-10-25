# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio
import models 

MESSAGES_RECEIVED_CHANNEL = 'messages received'
USERS_JOINED_CHANNEL = 'users joined'
AUTHU_JOINED_CHANNEL = 'authusers joined'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

database_uri = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app


db.create_all()
db.session.commit()

#users=['milkdad','glizzygod','shakeman221']
#newuser=users[1]


def emit_all_messages(channel):
    all_messages = [ \
        db_message.message for db_message \
        in db.session.query(models.Kashmessenger).all()
        ]
        
    socketio.emit(channel, {
        'allMessages': all_messages
    })
    

def emit_all_auth_users(channel):
    auth_users = [ \
        db_authu.name for db_authu \
        in db.session.query(models.AuthUser).all()
        ]
        
    socketio.emit(channel, {
        'allAuthU': auth_users
    })


def emit_all_users(channel):
    all_users = [ \
        db_user.user for db_user \
        in db.session.query(models.Kashusers).all()
        ]
    
    socketio.emit(channel, {
        'allUsers': all_users
    })
    
def push_new_user_to_db(name, auth_type):
    if name != "John Doe":
        db.session.add(models.AuthUser(name, auth_type));
        db.session.commit()
    
    
@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    socketio.emit('connected', {
        'test': 'Connected'
    })
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    emit_all_users(USERS_JOINED_CHANNEL)
    #emit_all_auth_users(AUTHU_JOINED_CHANNEL)
    

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

@socketio.on('new message input')
def on_new_message(data):
    print("Got an event for a new message input with data:", data)
    
    db.session.add(models.Kashmessenger(data["message"]));
    #db.session.add(models.Kashmessenger(data["user"]));
    db.session.commit();
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

@socketio.on('new user input')
def on_new_user(data):
    print("Got an event for a new USER input with data:", data)
    db.session.add(models.Kashusers(data["user"]));
    db.session.commit();
    
    #emit_all_users(USERS_JOINED_CHANNEL)
    
@socketio.on('new google user')
def on_new_google_user(data):
    print("Got an event for a new google user input with data:", data)
    push_new_user_to_db(data.name, models.AuthUserType.GOOGLE)
    
    
@app.route('/')

def index():
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    emit_all_users(USERS_JOINED_CHANNEL)

    models.db.create_all()
    
    return flask.render_template("index.html")

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
