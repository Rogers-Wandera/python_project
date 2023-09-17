from flask import Flask
from waitress import serve
from flask import request, render_template
from weather import get_current_weather

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/weather", methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city = 'Kampala'
    weather_data = get_current_weather(city)

    stat = int(weather_data['cod']);

    if not stat == 200:
       return f"City {city} not found"
    return render_template(
        "weather.html",
        title=weather_data['name'],
        status=weather_data['weather'][0]['description'],
        temp=f"{weather_data['main']['temp']:.2f}",
        feels_like=f"{weather_data['main']['feels_like']:.2f}",
    )


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port='8080')
