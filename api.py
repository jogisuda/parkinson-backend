from flask import Flask, request #import main Flask class and request object
from flask_cors import CORS
import glob
import numpy as np

from extractFeatures import extractFeatures

import os

#para próxima abordagem: testar converter em imagem e Deep Learning.

app = Flask(__name__) #create the Flask app

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route('/', methods=['POST']) #GET requests will be blocked
def index():
    #json_obj = request.get_json()
    sensorData = request.form
    print(request.get_json(), sensorData)
    #print("[*] REQ: *****************\n", sensorData["spiral"])
    print("FILE: ", request.files)
    spiral = np.array(request.json.get('spiral'))
    meander = np.array(request.json.get('meander'))
    diado = np.array(request.json.get('diado'))

    #save spiral, meander, diado in txt

    print("SPIRAL: {}\n".format(spiral))
    print("MEANDER: {}\n".format(meander))
    print("DIADO: {}\n".format(diado))

    #extract features
    feature_vector_spiral = extractFeatures(spiral)
    feature_vector_meander = extractFeatures(meander)
    feature_vector_diado = extractFeatures(diado)

    #print("SPIRAL: {}\n".format(spiral))
    #print("MEANDER: {}\n".format(meander))
    #print("DIADO: {}\n".format(diado))


    #classify
    #predicted_spiral = 
    return 'data received: \n{}'.format(sensorData)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) #run app in debug mode on port 5000
