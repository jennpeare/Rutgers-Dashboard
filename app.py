import flask, weather, food, quote, bus
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html", weather = weather.get_weather(), quote = quote.format_quote(quote.get_quote()))

@app.route("/test.html")
def test():
    return render_template("test.html",
      weather = weather.get_weather(),
      quote = quote.format_quote(quote.get_quote()),
      food = food.get_food_master(),
      bus_bcc = bus.get_predictions_for("Busch Campus Center"),
      bus_hill = bus.get_predictions_for("Hill Center"))

@app.route("/weather")
def get_weather():
    return flask.jsonify(weather.get_weather())

@app.route("/food")
def get_food():
    return flask.jsonify(food = food.get_food_master())

@app.route("/quote")
def get_quote():
    return flask.jsonify(quote.format_quote(quote.get_quote()))

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=8080)
