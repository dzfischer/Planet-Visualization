from flask import render_template, flash, redirect, url_for, request, jsonify
from datetime import datetime, date
from app import app, db



# --- imported from biodiversity -----

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
planets_table = Base.classes.planets


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

@app.route('/column/<title>')
def column(title):



    return 0;