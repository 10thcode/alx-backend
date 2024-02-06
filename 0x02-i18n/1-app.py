#!/usr/bin/env python3
"""
Creates a Flask application with babel i18n.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Sets Babel default configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """
    Handles / uri.
    """
    return (render_template("0-index.html"))
