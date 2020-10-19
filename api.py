from flask import Flask, request #import main Flask class and request object
from flask_cors import CORS

import os

app = Flask(__name__) #create the Flask app

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route('/', methods=['POST']) #GET requests will be blocked
def index():
    #json_obj = request.get_json()
    val1 = request.json
    return 'data received: \n{}'.format(val1)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) #run app in debug mode on port 5000
