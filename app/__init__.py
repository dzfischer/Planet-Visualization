from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

from app import routes, models