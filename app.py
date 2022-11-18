from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_HOST = "0.0.0.0"
API_PORT = 5500

# GET
@app.route("/", methods=["GET"])
def home():
    '''
    'Página inicial
    '''
    return "Proyecto FLASK"

@app.route("/json", methods=["GET"])
def json():
    '''
    'Prueba jsonify
    '''
    return jsonify(
        {
            "status" : "online",
            "int_num" : 4,
            "bool" : True,
            "list" : [1, "a", False]
        }
    )

if __name__ == "__main__":
    app.run(host=API_HOST, debug=True, port=API_PORT)