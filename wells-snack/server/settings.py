import os

API_VERSION = 'v1.0'
LISTEN_PORT = int(os.environ.get('LISTEN_PORT', 23360))

WIT_SERVER_ACCESS_TOKEN = os.environ.get('WIT_SERVER_ACCESS_TOKEN')
