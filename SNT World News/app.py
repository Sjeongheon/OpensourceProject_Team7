#!/usr/bin/python
from flask import Flask
from flask import render_template
from flask import request
from storefunction import *
import time
from random import randint
import sys
from elasticsearch import Elasticsearch

today = str(time.gmtime().tm_mday) + str(time.gmtime().tm_mon)+str(time.gmtime().tm_year)
integrationFuction(today)
MAX_show_num = 3 

es_host = "127.0.0.1"
es_port = "9200"

es = Elasticsearch([{'host':es_host, 'port':es_port}],timeout=30)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/world')
def world():
	
	return render_template('world.html', d1 = es.search(index = 'world')['hits']['hits'])

@app.route('/world1')
def world1():
	
	return render_template('world1.html',d1 = es.search(index = 'world')['hits']['hits'])

@app.route('/world2')
def world2():
	
	return render_template('world2.html',d1 = es.search(index = 'world')['hits']['hits'])

@app.route('/science')
def science():
	return render_template('science.html', d1 = es.search(index = 'science')['hits']['hits'])
@app.route('/science1')
def science1():
	return render_template('science1.html', d1 = es.search(index = 'science')['hits']['hits'])

@app.route('/science2')
def science2():
	return render_template('science2.html', d1 = es.search(index = 'science')['hits']['hits'])

@app.route('/health')
def health():
        return render_template('health.html', d1 = es.search(index = 'health')['hits']['hits'])

@app.route('/health1')
def health1():
        return render_template('health1.html', d1 = es.search(index = 'health')['hits']['hits'])

@app.route('/health2')
def health2():
        return render_template('health2.html', d1 = es.search(index = 'health')['hits']['hits'])


if __name__ == '__main__':
	app.run()

