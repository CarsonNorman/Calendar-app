from flask_app import app
from flask import request

@app.route("/appointment/create", methods=['POST'])
def handleCreate():
    print(request)
    return request.json['hello']