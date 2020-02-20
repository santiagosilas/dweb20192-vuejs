from flask import Flask

api = Flask(__name__)
api.debug = True

from app import routes