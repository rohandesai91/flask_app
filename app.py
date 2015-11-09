# from flask import Flask, request
# from flask_request_params import bind_request_params
# app = Flask(__name__)
# app.secret_key = 'secret'
# app.before_request(bind_request_params)


@app.route("/")
def main():
	return "Test Page"

# @app.route('/flu')
# def fun():
# 	return 'Influenza'


# @app.route('/echo/<path>', methods=['GET', 'POST'])
# def echo(path):
#     return request.params


# if __name__ == "__main__":
#     app.run()

from flask import Flask, request, render_template, jsonify
from flask_request_params import bind_request_params

import urllib
import json

myList = []
a = "features"
b = "properties"
c = "title"

app = Flask(__name__)
app.secret_key = 'secret'
# bind rails like params to request.params
app.before_request(bind_request_params)

# just return request.params
@app.route('/api/vi', methods=['GET'])
def getQ():
	global myList
	x = request.args.get('a')

	with open("sym.json") as json_file:
		theJSON = json.load(json_file)
		str = ""
		for i in theJSON[a]:
			if i[b][x] >= 5.0:
				str += i[b][c] + " "
		return str
	
app.run(host='0.0.0.0', port=5600)
