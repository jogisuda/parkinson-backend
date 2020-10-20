from flask import Flask, request #import main Flask class and request object
from flask_cors import CORS

import os

#para próxima abordagem: testar converter em imagem e Deep Learning.

app = Flask(__name__) #create the Flask app

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route('/', methods=['POST']) #GET requests will be blocked
def index():
    #json_obj = request.get_json()
    val1 = request.json
    print("[*] REQ: *****************\n", val1)
    spiral = request.json.get('spiral')
    meander = request.json.get('meander')
    diado = request.json.get('diado')

    #save spiral, meander, diado in txt

    print("SPIRAL: {}\n".format(spiral))
    print("MEANDER: {}\n".format(meander))
    print("DIADO: {}\n".format(diado))

    #extract features
    #feature_vector_spiral = getFeatures(spiral)
    #feature_vector_meander = getFeatures(meander)
    #feature_vector_diado = getFeatures(diado)

    #classify
    #predicted_spiral = 
    return 'data received: \n{}'.format(val1)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) #run app in debug mode on port 5000
