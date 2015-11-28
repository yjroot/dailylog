from flask import Flask
from werkzeug.local import LocalProxy

from .db import get_session


app = Flask(__name__)


@LocalProxy
def session():
    return get_session()


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World'
