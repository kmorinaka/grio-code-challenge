import os
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

from script import api_call
# import requests

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "development")

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

app.jinja_env.undefined = StrictUndefined


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/results", methods=["GET"])
def show_results():
	user_one = str(request.args.get('username1'))
	user_two = str(request.args.get('username2'))
	results_one = api_call(user_one)
	results_two = api_call(user_two)

	if results_one['total_stars'] > results_two['total_stars']:
		winner = results_one['username']
	else: 
		winner = results_two['username']	

	return render_template("results.html", results_one=results_one,
		results_two=results_two, winner=winner)


if __name__ == "__main__":
	app.debug = True
	DebugToolbarExtension(app)
	app.run()
