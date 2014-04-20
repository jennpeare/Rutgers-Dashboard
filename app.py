import flask, weather, food, quote
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html", weather = weather.get_weather(), quote = quote.format_quote(quote.get_quote()))
    #return render_template("index.html", weather = "weather", quote = "quote")

@app.route("/test.html")
def test():
    #return render_template("index.html", weather = weather.get_weather(), quote = quote.format_quote(quote.get_quote()))
    return render_template("test.html",
      weather = weather.get_weather(),
      quote = quote.format_quote(quote.get_quote()),
      food = food.get_food_master()
      )

@app.route("/weather")
def get_weather():
    return flask.jsonify(weather.get_weather())

@app.route("/food")
def get_food():
    #return flask.jsonify(food.get_food_all())
    return flask.jsonify(food = food.get_food_master())
@app.route("/quote")
def get_quote():
    return flask.jsonify(quote.format_quote(quote.get_quote()))

if __name__ == "__main__":
    app.run(debug=True)
