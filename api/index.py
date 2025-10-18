import time

from flask import Flask
from flask_cors import CORS, cross_origin

from db import init_db

app = Flask(__name__)
CORS(app)

init_db()

@app.route("/api/shorten")
@cross_origin()
def shorten_url():
    return {'time': time.time()}
