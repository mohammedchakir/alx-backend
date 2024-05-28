#!/usr/bin/env python3
"""
A Flask app with Babel for language support.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Flask app configurations.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    The index route that renders the welcome page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
