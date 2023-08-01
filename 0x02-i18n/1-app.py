#!/usr/bin/env python3
"""
Basic Flask app that serves an index page.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
"""Instantiate the Babel object and set the default locale and timezone"""
babel = Babel(app)


"""Create the Config class with LANGUAGES attribute"""
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def index():
    """
    hello world
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
