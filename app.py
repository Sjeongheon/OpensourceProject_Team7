#!/usr/bin/python
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/world')
def world():
	return render_template('world.html')

@app.route('/tech')
def tech():
	return render_template('tech.html')

@app.route('/health')
def health():
        return render_template('health.html')


if __name__ == '__main__':
	app.run()
