from flask import render_template, flash, redirect, url_for, request, jsonify
from datetime import datetime, date
from app import app, db
from app.models import Planets
import sqlalchemy
from sqlalchemy.ext.automap import automap_base


# # --- imported from biodiversity -----

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# planets_table = Base.classes.planets


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
    sql_query = db.session.query(Planets.rowid,
                                 Planets.pl_name,
                                 Planets.pl_hostname,
                                 f'planets.{title}').all()
    sql_query_dict = [row._asdict() for row in sql_query]
    return jsonify(results=sql_query_dict)

<<<<<<< HEAD
@app.route('/our_data')
def our_data():
    return render_template('our_data.html', title='Our Data')
=======

@app.route('/dchartcolumns')
def columns():
    sql_query = db.session.query(Planets.st_teff,
                                 Planets.st_logg,
                                 Planets.pl_eqt,
                                 Planets.st_mass,
                                 Planets.st_rad).all()
    columns = [row._asdict() for row in sql_query]
    #return jsonify(results=sql_query_dict)
    return jsonify(columns)


@app.route('/ProjectPlanets')
def ProjectPlanets():
    return render_template('D3.html', title='Planets!')
>>>>>>> 52c73fad661b26a5e0a144c422877e23fc1f07b8
