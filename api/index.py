import time
import uuid

from flask import Flask, session
from flask_cors import CORS, cross_origin
from instance.config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

@app.route("/")
@cross_origin()
def index():
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())
    return session["user_id"], 200


@app.route("/api/shorten")
@cross_origin()
def shorten_url():
    return {'time': time.time()}
