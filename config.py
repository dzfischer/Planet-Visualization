import os


class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or f'postgres://hbksjnnybdgxmx:a09177f34f8e02fbf9a05271e211f6b83b351dd55b375c0652edadf540b2df53@ec2-107-21-216-112.compute-1.amazonaws.com:5432/ddct29qfmo6dve'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
