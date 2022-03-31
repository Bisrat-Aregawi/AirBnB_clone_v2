#!/usr/bin/python3
"""Start Flask app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greetingHBNB():
    """return greet message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return `HBNB` string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cMessage(text=None):
    """return `C` followed by text"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
