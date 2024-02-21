#!/usr/bin/python3
"""Startcation.

Then lport 5000.
Routes:
    /: DisplayNB!'.
    /hbnb: DisNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Dispo"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """DisBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
