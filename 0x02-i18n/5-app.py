#!/usr/bin/env python3
"""
This module sets up a basic Flask app with Babel for language support.
It includes a mocked user login system and displays messages based
on login state.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Returns a user dictionary or None if the ID cannot be found or if
    login_as was not passed.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Finds a user if any, and sets it as a global on flask.g.user before
    each request.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Selects the best matching locale according to the request's
    'Accept-Language' headers or the 'locale' URL parameter,
    or the user's preferred locale.
    """
    user = g.get('user')
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The index route renders the index.html template.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
