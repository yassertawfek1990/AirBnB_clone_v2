#!/usr/bin/python3
"""Staration.

The apl0.
Routes:
    /: Displays 'HelloHBNB!'.
    /hbnb: DisplayHBNB'.
    /c/<text>: Displaxt>.
    /python/(<text>): Dispt>.
    /number/<n>: Displays eger.
    /number_template/<n>: Displ
    /number_odd_or_even/<n>: Displaysteger.
        - Stateswhether<n>ebody.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """DisplaysHBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """DisplayHBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displaytext>

    Replaces slashes."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays<text>

    Replace."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displayinteger."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displaysinteger.

    Displabody."""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displayinteger.

    Statebody."""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
