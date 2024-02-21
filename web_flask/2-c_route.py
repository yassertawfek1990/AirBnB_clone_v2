#!/usr/bin/python3
"""StartsaFlaapplication.

The applicati00.
Routes:
    /: Displays 'HelloHBNB!'.
    /hbnb: DisplayHBNB'.
    /c/<text>: Die otext>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """DisplayHBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displ"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displatext>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
