import flask
import requests
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET']) #if the server receive get request to the address / , he execute home function
def home():
    return render_template("HTML1.html")
@app.route('/weather', methods = ["POST"]) #if the server receive to the address /weather he execute index function
def index():
    cityName = request.form.get("textFieldId")
    print(cityName)
    key = "YZLU5TMAGQCDQMMNSJ2CT2HYE"
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cityName}/next7days?key={key}'
    response = requests.get(url) # http get request
    jason = response.json() #convert to jason
    # in the next lines, will be formatting data
    # array of tuples = [(datetime,temp,humidity,morning/evening)],morning = 8:00, evening = 20:00
    forecast = []
    for day in jason["days"]:
        celsius1 = round((day["hours"][8]['temp'] - 32) * 5/9,2)
        celsius2 = round((day["hours"][20]['temp'] - 32) * 5 / 9,2)
        forecast.append((day['datetime'],celsius1,day["hours"][8]['humidity'],"morning"))
        forecast.append((day['datetime'],celsius2, day["hours"][20]['humidity'],"evening"))
    # returns html2.html with data
    return render_template("html2.html",my_data = forecast, cityName = cityName)

if __name__ == '__main__':
    app.run()
    