from flask import Flask, jsonify, request, Response
from fungogo import app
from .model import ChatBot
import time

@app.route("/"+app.config['API_VERSION']+"/", methods=['GET'])
def helloWorld():
	return jsonify({'hello': 'world'})

@app.route("/"+app.config['API_VERSION']+"/speak", methods=['POST'])
def cb():
	cb = ChatBot()
	body = request.get_json()

	return jsonify({
		"status": "OK",
		"data": cb.message(body.get('text'))
	})
