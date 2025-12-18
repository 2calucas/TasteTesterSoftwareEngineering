'''
Created on 18/12/2025
Author: Cal Lucas
Version: 0.1
Description: A simple Flask application to run Taste Tracker website.
'''

from flask import Flask, render_template   # use render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Render the template and pass data into it
    return render_template('index.html', status='ok')

if __name__ == '__main__':
    app.run(debug=True, port=5000)