from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# original app configuration from config file
# app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///static/data/planets.sqlite"
db = SQLAlchemy(app)
# db.Model.metadata.reflect(db.engine)

from app import routes, models