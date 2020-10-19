from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    return 'data received: \n{}'.format(request.get_json())


if _name == '__main_':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
