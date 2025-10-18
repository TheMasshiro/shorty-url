import time

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'

@app.route("/api/shorten")
@cross_origin()
def shorten_url():
    return {'time': time.time()}
