#!/usr/bin/python3
"""Start Flask App"""
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


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>/', strict_slashes=False)
def pythonMessage(text):
    """return `python` followed by text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>/', strict_slashes=False)
def numberViewer(n):
    """Return string if n is number"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
