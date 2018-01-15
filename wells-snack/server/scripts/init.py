if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        rootPath = path.abspath(path.join(path.dirname(path.abspath(__file__)), '../'))
        sys.path.append(rootPath)

from fungogo import SETTINGS
import requests

headers = {'Authorization': 'Bearer '+SETTINGS["WIT_SERVER_ACCESS_TOKEN"]}
payload = []

payload.append({"text": '哈囉', "entities": [{"entity": 'intent', "value": 'greeting'}]})
payload.append({"text": '你好', "entities": [{"entity": 'intent', "value": 'greeting'}]})
payload.append({"text": 'Hi', "entities": [{"entity": 'intent', "value": 'greeting'}]})
payload.append({"text": 'Hey', "entities": [{"entity": 'intent', "value": 'greeting'}]})

payload.append({"text": '掰掰', "entities": [{"entity": 'intent', "value": 'bye'}]})
payload.append({"text": '再見', "entities": [{"entity": 'intent', "value": 'bye'}]})
payload.append({"text": 'see you', "entities": [{"entity": 'intent', "value": 'bye'}]})
payload.append({"text": 'byebye', "entities": [{"entity": 'intent', "value": 'bye'}]})

r = requests.post(
	'https://api.wit.ai/entities?v=20170416',
	headers=headers,
	json={
		"doc":"intent",
		"id":"intent",
		"values":[{"value":"greeting"}, {"value":"bye"}]}
)
print(r.text)

r = requests.post(
		'https://api.wit.ai/samples?v=20170416',
		headers=headers,
		json=payload
	)
print(r.text)

r = requests.get(
		'https://api.wit.ai/message?v=20170416',
		headers=headers,
		params={
			"q": "掰掰"
		}
	)
print(r.text)

