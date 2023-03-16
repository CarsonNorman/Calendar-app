from flask_app import app
from flask import request
from flask_app.models.patient_model import Patient

@app.route("/create/patient", methods=['POST'])
def handleCreate():
    data = request.form
    print(data)
    patient = Patient.create(request.form)
    print(f'patient {patient}')
    return f'{patient}'
@app.route("/read/patient", methods=['GET'])
def handleReadAllPatients():
    patients = Patient.readAll()
    return f'{patients}'