'''
Created on 18/12/2025
Author: Cal Lucas
Version: 0.3
Description: A simple Flask application to run Taste Tracker website.
'''

from flask import Flask, render_template   # use render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/maps')
def maps():
    return render_template('maps_page.html')

@app.route('/lists')
def lists():
    return render_template('lists.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)