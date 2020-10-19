from flask import Flask, request #import main Flask class and request object
import os

app = Flask(__name__) #create the Flask app

@app.route('/', methods=['POST']) #GET requests will be blocked
def json_example():
    return 'data received: \n{}'.format(request.get_json())


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=5000) #run app in debug mode on port 5000
