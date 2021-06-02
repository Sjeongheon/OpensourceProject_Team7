#!/usr/bin/python
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return render_template('home.html') 

@app.route('/world',methods=['POST'])
def world():
	return render_template('world.html')

@app.route('/us',methods=['POST'])
def us():
	return render_template('us.html')

@app.route('/politics',methods=['POST'])
def politics():
        return render_template('politics.html')


if __name__ == '__main__':
	ipaddr="127.0.0.1"
	print("Starting the service with ip_adr="+ipaddr)
	app.run(host=ipaddr, port=5000)
