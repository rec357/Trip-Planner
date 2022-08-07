from flask import Flask

app = Flask(__name__)

@app.route("/")
def trip_planner():
    return "<h1>Trip Planner</h1>"