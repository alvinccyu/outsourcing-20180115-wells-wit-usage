from werkzeug.contrib.fixers import ProxyFix
from flask import Flask

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_pyfile('../settings.py')
SETTINGS = app.config

import fungogo.chatbot.route

