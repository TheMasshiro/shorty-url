import time

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def index():
    from db import check_database

    if not  check_database():
        return "Failed"
    return "Success"



@app.route("/api/shorten")
@cross_origin()
def shorten_url():
    return {'time': time.time()}
