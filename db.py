import os
import sqlite3

from flask import g

from api.index import app

DATABASE = os.path.join(os.getcwd(), "database.db")


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(_):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if not os.path.exists(DATABASE):
    with app.app_context():
        db = get_db()
        with app.open_resource(os.path.join("schema.sql"), mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()
