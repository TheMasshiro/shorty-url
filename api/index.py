import time

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

try:
    from db import init_db
    with app.app_context():
        init_db()
except Exception as e:
    import sys
    print(f"Database initialization failed: {e}", file=sys.stderr)

@app.route("/")
def health():
    return {"status": "ok"}

@app.route("/api/shorten", methods=["POST"])
@cross_origin()
def shorten_url():
    data = request.get_json()
    url = data.get("url")
    return jsonify({"shortUrl": f"{url}-{int(time.time())}"})
