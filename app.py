"""
A basic flask application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return a simple hello world"""
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Greet the user"""
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<temp>')
def f(temp='0'):
    """Convert Celsius to fahrenheit"""
    try:
        return f"{temp}C is {calculate_fahrenheit_from_celsius(float(temp))}F"
    except ValueError:
        return f"{temp} is not a valid number!"


def calculate_fahrenheit_from_celsius(celsius):
    """Convert from Celsius to Fahrenheit"""
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
