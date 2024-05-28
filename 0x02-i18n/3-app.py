#!/usr/bin/env python3
"""
A Flask app with Babel for internationalization,
locale selection, and translations.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class for Flask app configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Selects the best matching language for the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The index route that renders the welcome page.
    """
    return render_template('3-index.html',
                           home_title=_("Welcome to Holberton"),
                           home_header=_("Hello world!"))


if __name__ == '__main__':
    app.run(debug=True)
