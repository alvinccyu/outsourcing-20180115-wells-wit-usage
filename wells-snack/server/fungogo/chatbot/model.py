from fungogo import SETTINGS
import requests
import json

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatBot(object):
	def __init__(self, arg={}):
		super(ChatBot, self).__init__()

	def message(self, text):
		headers = {'Authorization': 'Bearer '+SETTINGS["WIT_SERVER_ACCESS_TOKEN"]}
		r = requests.get(
				'https://api.wit.ai/message?v=20170416',
				headers=headers,
				params={
					"q": text
				}
			)
		response = json.loads(r.text)
		logger.info("wit response %s", response)

		intent = response.get('entities', {}).get('intent')
		if intent:
			firstIntent = intent[0]
			return "#%s Confidence(%s)" % (firstIntent['value'], firstIntent['confidence'])
		else:
			return "Echo => "+text
