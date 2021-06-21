#!/usr/bin/python
from flask import Flask
from flask import render_template
from flask import request
from main import *

d = integrationFunction()


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/world')
def world():
	
	return render_template('world.html', d1 = d[0])

@app.route('/world1')
def world1():
	
	return render_template('world1.html', d1 = d[0])

@app.route('/world2')
def world2():
	
	return render_template('world2.html', d1 = d[0])

@app.route('/science')
def science():
	return render_template('science.html', d1 = d[1])
@app.route('/science1')
def science1():
	return render_template('science1.html', d1 = d[1])

@app.route('/science2')
def science2():
	return render_template('science2.html', d1 = d[1])

@app.route('/health')
def health():
        return render_template('health.html', d1 = d[2])

@app.route('/health1')
def health1():
        return render_template('health1.html', d1 = d[2])

@app.route('/health2')
def health2():
        return render_template('health2.html', d1 = d[2])


if __name__ == '__main__':
	app.run()
