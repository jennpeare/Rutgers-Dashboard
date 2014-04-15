import flask, weather, food, quote
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
	weather = "hello"
	return render_template('index.html', weather=weather)

@app.route("/weather")
def get_weather():
    return flask.jsonify(current_cond = weather.get_weather())

@app.route("/food")
def get_food():
    return flask.jsonify(food.get_food_all())

@app.route("/quote")
def get_quote():
    return flask.jsonify(quote.format_quote(quote.get_quote()))

if __name__ == "__main__":
    app.run(debug=True)
