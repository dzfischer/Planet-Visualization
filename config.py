import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:South8*paw@localhost:5432/consumption'
    SQLALCHEMY_TRACK_MODIFICATIONS = False