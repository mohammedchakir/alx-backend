#!/usr/bin/env python3
"""
This module sets up a basic Flask app with Babel for language support.
It includes a locale selector to determine the best match for supported
languages and allows forcing a locale via URL parameters.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class to hold configuration for the Flask app.
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
    Selects the best matching locale according to the request's
    'Accept-Language' headers or the 'locale' URL parameter.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The index route renders the index.html template.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
