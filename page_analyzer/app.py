from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_hexlet():
    return 'Welcome to Page Analyzer!'


@app.route('/page')
def page():
    return render_template('index.html')
