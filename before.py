""" simple page """

import os
import requests
import json
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def main():
    """ renders index template """
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():
    global response, parse_responce, number
    number = request.form["number"]
    if request.method == "POST":
        response = requests.get(
            "https://interview.dev.lab.o2online.de/api/" + number)

        parse_responce = str(response.json()['a']) + response.json()[
            'op'] + str(response.json()['b'])

        calculate()
        return render_template("index.html", exercise=parse_responce, number=number)


def calculate():
    global res
    if response.json()['op'] == "+":
        res = response.json()['a'] + response.json()['b']
    elif response.json()['op'] == "-":
        res = response.json()['a'] - response.json()['b']
    elif response.json()['op'] == "*":
        res = response.json()['a'] * response.json()['b']


@app.route("/calc", methods=["POST"])
def calc():
    answer = request.form["answer"]
    if answer == str(response.calculate()):
        right = "Yes! It is " + str(response.calculate())
    else:
        right = "No, it is " + str(response.calculate())

    return render_template("index.html", answer=answer, right=right, exercise=parse_responce, result=res, number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=int(os.getenv('PORT', 5000)))
