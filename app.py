import api
import os
from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route("/")
def main():
    """ renders index template """
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():
    global response, number
    number = request.form["number"]
    if request.method == "POST":
        data = requests.get(
            "https://interview.dev.lab.o2online.de/api/" + number).json()
        response = api.API(data)
        return render_template("index.html", exercise=response.exercise(), number=number)


@app.route("/calc", methods=["POST"])
def calc():
    answer = request.form["answer"]
    if answer == str(response.calculate()):
        right = "Yes! It is " + str(response.calculate())
    else:
        right = "No, it is " + str(response.calculate())

    return render_template("index.html", answer=answer, right=right, exercise=response.exercise(), result=response.calculate(), number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=int(os.getenv('PORT', 5000)))
