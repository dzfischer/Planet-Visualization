from flask import render_template, flash, redirect, url_for, request, jsonify
from datetime import datetime, date
from app import app, db


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Planets!')

@app.route('/json_stats')
def json_stats():
    return 'hello'


@app.route('/json_monthly')
def json_monthly():
    return 'testing'