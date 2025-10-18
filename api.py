import time
import uuid

from flask import session
from flask_cors import cross_origin

from api.index import app


@app.route("/", methods=["GET"])
@cross_origin()
def index():
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())
    return session["user_id"], 200


@app.route("/api/shorten")
@cross_origin()
def shorten_url():
    return {'time': time.time()}
