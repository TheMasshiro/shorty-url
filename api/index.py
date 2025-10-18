from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'

@app.route('/about')
@cross_origin()
def about():
    return 'About'
