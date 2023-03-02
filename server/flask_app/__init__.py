from flask import Flask
app = Flask(__name__)
app.secret_key='ItsASecretINIT'
from flask_cors import CORS
CORS(app)