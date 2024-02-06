#!/usr/bin/env python3
"""
Creates Flask application.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Handles / uri.
    """
    return (render_template("0-index.html"))
