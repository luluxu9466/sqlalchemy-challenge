# 1. import Flask
from flask import Flask
from flask import jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from sqlalchemy import desc

import datetime as dt
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# connect to climate.ipynb
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# 3. Define what to do when a user hits the index route
@app.route("/")
# List all routes that are available
def home():
    return (
        f"Welcome to the Precipitation API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


# 4. Define what to do when a user hits the /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
def precipitation():
    prcp = session.query(Measurement.date, Measurement.prcp)
    prcp_dict = dict(prcp)
    return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
# return a JSON list of stations from the dataset
def stations():
    station_list = session.query(Station.station, Station.name).all()
    return jsonify(station_list)
    

@app.route("/api/v1.0/tobs")
# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
def tobs():
    date = []
    for _ in session.query(Measurement.date).order_by(Measurement.date.desc()):
        date.append(_.date)
    last_date = date[1]
    one_year_ago = datetime.fromisoformat(last_date) - relativedelta(years=1)
    tobs = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= one_year_ago).\
            order_by(Measurement.date).all()
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start.
# Calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
def startdate(start):
    tobs = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    tobs_dict = dict()
    tobs_dict["Min Temp"] = tobs[0][0]
    tobs_dict["Avg Temp"] = tobs[0][1]
    tobs_dict["Max Temp"] = tobs[0][2]
    return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>/<end>")
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range.
# Calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
def startend(start, end):
    tobs = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    tobs_dict = dict()
    tobs_dict["Min Temp"] = tobs[0][0]
    tobs_dict["Avg Temp"] = tobs[0][1]
    tobs_dict["Max Temp"] = tobs[0][2]
    return jsonify(tobs_dict)

if __name__ == "__main__":
    app.run(debug=True)
