from flask import Flask
from database.database import db_session, init_db

from controllers import register_controllers

init_db()

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

register_controllers(app)