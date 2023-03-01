from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/days")
def days():
    return {"days":["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}

if __name__ == "__main__":
    app.run(debug=True)