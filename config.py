import os


class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///static/data/planets.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
