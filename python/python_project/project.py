import flask
import requests
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return flask.send_file("HTML1.html")

@app.route('/weather', methods = ["POST"])
def index():
    cityName = request.form.get("place")
    print(cityName)
    key = "YZLU5TMAGQCDQMMNSJ2CT2HYE"
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cityName}/next7days?key={key}'
    response = requests.get(url)
    jason = response.json() #convert to jason
    celsius = (jason["days"][0]["temp"]-32) /1.8
    print(jason["days"][0]["datetime"])
    print(celsius)
    print(jason["days"][0]["humidity"])









if __name__ == '__main__':
    app.run()
    