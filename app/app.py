from flask import Flask
from api import api
from websocket import socketio
from models import db
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin123@localhost:5432/watch_party_db"

db.init_app(app)

app.register_blueprint(api)
socketio.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)