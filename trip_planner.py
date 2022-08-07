from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def trip_planner():
        if request.args.get("zip"):
                return get_trip_data(request.args.get("zip"))
        else:
                return """<h1>Trip Planner</h1>
                        <form>
                                <label for="zip">Please input the zipcode of where you wish to travel:</label>
                                <input type="text" id="zip" name="zip"></br>
                                <input type="submit" value="Submit">
                        </form>
                """


def get_trip_data(zip):
        data =  """
                Here are your results for your trip to  {}
        """
        data = data.format(zip)
        
        # Hey Regina and Rita, you can make your API calls here and append to the data string
        # to display on the screen. ie below, try to make another function to get this data
            
        data = data + getHotels(zip)
        data = data + getRestaurants(zip)
                                
        return data
                   

def getHotels(zip):
        #use zip to get data
        return "<br/>Here are some hotels"

def getRestaurants(zip):
    #use zip to get data
    return "<br/>Here are some Restaurants"