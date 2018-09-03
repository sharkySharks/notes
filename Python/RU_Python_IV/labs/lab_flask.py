#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_flask` -- serving up REST
=========================================

LAB_FLASK Learning Objective: Learn to serve RESTful APIs using the Flask library
::

 a. Using Flask create a simple server that serves the following string for the root route ('/'):
  "<h1>Welcome to my server</h1>"

 b. Add a route for "/now" that returns the current date and time in string format.

 c. Add a route that converts Fahrenheit to Centigrade and accepts the value to convert
    in the url.  For instance, /fahrenheit/32.0 should return "0.0"

 d. Add a route that converts Centigrade to Fahrenheit and accepts the value to convert
    in the url.  For instance, /centigrade/0.0 should return "32.0"

"""

import datetime
from flask import Flask
from flask import render_template


def f_to_c(f):
    return 5.0 / 9.0 * (f - 32.0)

def c_to_f(c):
    return (9.0 / 5.0 * c) + 32.0


app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('lab_flask_template.html')
    # return "<h1>Welcome to my server</h1>"    # can also do it this way


@app.route('/now')
def now():
    return datetime.datetime.now().ctime()


@app.route('/fahrenheit/<int:f>')
@app.route('/fahrenheit/<float:f>')
def from_fahrenheit(f):
    return str(f_to_c(f))


@app.route('/centigrade/<int:c>')
@app.route('/centigrade/<float:c>')
def from_centigrade(c):
    return str(c_to_f(c))



if __name__ == '__main__':
    app.run()
