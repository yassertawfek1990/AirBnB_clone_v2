#!/usr/bin/python3
"""Startplication.

The000.
Routes:
    /: DisplaysBNB!'.
    /hbnb: DisplaysBNB'.
    /c/<text>: Displaytext>.
    /python/(<text>): Displays<text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displa"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """DisplayHBNB."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displ<text>.

    Replashes."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays <text>.

    Replacelashes."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
