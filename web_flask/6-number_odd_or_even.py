#!/usr/bin/python3
"""Start Flask App"""
from flask import Flask
from flask.templating import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greetingHBNB():
    """Return greet message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return `HBNB` string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cMessage(text=None):
    """Return `C` followed by text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>/', strict_slashes=False)
def pythonMessage(text):
    """Return `python` followed by text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>/', strict_slashes=False)
def numberViewer(n):
    """Return string if n is number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def showHTML(n):
    """Render html page if n is integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def showEvenOddHTML(n):
    """Render html page if n is integer and determine evennes"""
    evenness = ''
    evenness = 'even' if n % 2 == 0 else 'odd'
    return render_template(
        '6-number_odd_or_even.html',
        num=n,
        evenness=evenness
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
