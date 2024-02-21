#!/usr/bin/python3
"""Startpplication.

The applicatio5000.
Routes:
    /: DisplaloHBNB!'.
    /hbnb: DispHBNB'.
    /c/<text>: Displaext>.
    /python/(<text>): Disp<text>.
    /number/<n>: Displainteger.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displa<text>.

    Replachs"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displayst>.

    Replacesslashes."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displayr."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
