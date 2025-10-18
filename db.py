import os

import psycopg2
from flask import g
from psycopg2.extras import RealDictCursor

from api.index import app

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return db

@app.teardown_appcontext
def close_connection(_):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

def check_database():
    """Initialize database schema"""
    try:
        db = get_db()
        cursor = db.cursor()
        with app.open_resource("schema.sql", mode="r") as f:
            cursor.execute(f.read())
        db.commit()
        return True
    except Exception:
        return False
