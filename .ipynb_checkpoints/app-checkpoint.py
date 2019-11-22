# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
# List all routes that are available
def home():
    return (
        f"Welcome to the Percipitation API!<br/>"
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


@app.route("/api/v1.0/stations")
# return a JSON list of stations from the dataset
def stations():
    

@app.route("/api/v1.0/tobs")
# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
def tobs():

@app.route("/api/v1.0/<start>")
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start.
# Calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
def start(start):

@app.route("/api/v1.0/<start>/<end>")
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range.
# Calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
def startend(start, end)

if __name__ == "__main__":
    app.run(debug=True)
