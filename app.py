from flask import Flask
from flask_cors import CORS
from routes.servo import servo

app = Flask(__name__)
cors = CORS(app, resources={'/*':{'origins': 'http://localhost:3000'}}) 

app.register_blueprint(servo)
