from flask import Flask

app = Flask(__name__)

@app.route("/")
def trip_planner():
    return """<h1>Trip Planner</h1>
        <form>
            <label for="Zipcode"> Please input the zipcode of where you wish to travel:</label><br>
             <input type="text" id="Zipcode" name="Zipcode"><br>
        </form>

    """