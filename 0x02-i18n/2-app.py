#!/usr/bin/env python3
"""
Creates a Flask application with babel i18n.
"""
from flask import Flask, render_template, request
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
    return (render_template("3-index.html"))


@babel.localeselector
def get_locale():
    """
    Gets the best matched language
    """
    return (request.accept_languages.best_match(app.config["LANGUAGES"]))
