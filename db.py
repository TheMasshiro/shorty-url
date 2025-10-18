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
    """Initialize database schema if tables don't exist"""
    try:
        with app.app_context():
            db = get_db()
            cursor = db.cursor()

            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'urls'
                );
            """)
            table_exists = cursor.fetchone()[0]

            if not table_exists:
                with app.open_resource("schema.sql", mode="r") as f:
                    cursor.execute(f.read())
                db.commit()
                return True
    except Exception as e:
        print(f"Database check error: {e}")
        return False
    return False
