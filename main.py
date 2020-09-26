# This is a sample Flask project

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask

app = Flask(__name__)


@app.route('/')
def print_hi():
    return '<h1>Hi<h1>'


@app.route('/<name>')
def print_name(name):
    return f'<h1>Hi {name}<h1>'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
