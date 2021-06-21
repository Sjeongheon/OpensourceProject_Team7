from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/health')
def health():
	return render_template('health.html')

@app.route('/tech')
def tech():
	return render_template('tech.html')

@app.route('/world')
def world():
	return render_template('world.html')

if __name__ == "__main__":
	ipaddr="127.0.0.1"
	print("Starting the service with ip_adr="+ipaddr)
	app.run(host=ipaddr, port=5000)


