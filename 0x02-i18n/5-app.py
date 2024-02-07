#!/usr/bin/env python3
"""
Creates a Flask application with babel i18n.
"""
from flask import Flask, render_template, request, g
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
    return (render_template("5-index.html"))


@babel.localeselector
def get_locale():
    """
    Gets the best matched language
    """
    language = request.args.get("locale")
    if (language in app.config["LANGUAGES"]):
        return (language)

    return (request.accept_languages.best_match(app.config["LANGUAGES"]))


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


def get_user():
    """
    Gets a user.

    Returns:
	A user dictionary.
    """
    id = request.args.get('login_as', None)
    if (id is not None and int(id) in users.keys()):
        return users.get(int(id))

    return (None)


@app.before_request
def before_request():
    """
    Finds a user
    """
    g.user = get_user()
