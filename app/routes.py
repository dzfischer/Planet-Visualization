from flask import render_template, flash, redirect, url_for, request, jsonify
from datetime import datetime, date
from app import app, db
from app.models import Planets
import sqlalchemy
from sqlalchemy import func
from sqlalchemy.ext.automap import automap_base


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Planets!')


@app.route('/column/<title>')
def column(title):
    sql_query = db.session.query(Planets.rowid,
                                 Planets.pl_name,
                                 Planets.pl_hostname,
                                 f'planets.{title}').all()
    sql_query_dict = [row._asdict() for row in sql_query]
    return jsonify(results=sql_query_dict)


@app.route('/our_data')
def our_data():
    return render_template('our_data.html', title='Our Data')


@app.route('/dchartcolumns')
def columns():
    sql_query = db.session.query(Planets.st_teff,
                                 Planets.st_logg,
                                 Planets.pl_eqt,
                                 Planets.st_mass,
                                 Planets.st_rad).all()
    columns = [row._asdict() for row in sql_query]
    return jsonify(columns)


@app.route('/ProjectPlanets')
def ProjectPlanets():
    return render_template('D3.html', title='Planets!')


# To create route to html page
@app.route('/plotlyprojectplanets')
def PlotlyProjectPlanets():
    return render_template('plotly.html', title='Plotly Planets!')


@app.route('/planetdiscovery_number')
def plotlydata():
    results = db.session.query(func.count(Planets.pl_name).label('num_planets'),
                               Planets.pl_disc).group_by(Planets.pl_disc).all()
    # sort list of tuples in annual order for graph
    results.sort(key=lambda tup: tup[1])

    # creating lists from query results
    # to turn strings in tuples into intergers
    listofresults = list(
        zip(*[[int(result) for result in tup] for tup in results]))

    year_disc = list(listofresults[1])
    num_planets = list(listofresults[0])

    # Generate the plot trace
    trace = {
        "x": year_disc,
        "y": num_planets,
        "type": "bar",
        "color": "'rgb(142,124,195)'"
    }

    return jsonify(trace)


@app.route('/planetdiscovery_dist')
def plotlydata_1():

    results_1 = db.session.query(func.max(Planets.gaia_dist).label('max_gaia_dist'),
                                 Planets.pl_disc).group_by(Planets.pl_disc).all()
    # sort list of tuples in annual order for graph
    results_1.sort(key=lambda tup: tup[1])

    """ Creating lists from query results"""
    listofresults_gaia = list(zip(*[[result for result in tup]
                                    for tup in results_1]))  # to turn strings in tuples into intergers
    # removed int() due to null values in dataset

    """ Creating lists from query results"""
    gaia_edit = list(listofresults_gaia[0])
    gaia_edit[1] = 0
    gaia_edit[2] = 0
    gaia_dist_value = gaia_edit
    year_disc_gaia = list(listofresults_gaia[1])

    # Generate the plot trace
    trace = {
        "x": year_disc_gaia,
        "y": gaia_dist_value,
        "type": "bar",
        "color": "'rgb(142,124,195)'"
    }

    return jsonify(trace)
