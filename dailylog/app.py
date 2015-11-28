from flask import Flask, request
from werkzeug.local import LocalProxy

from .db import get_session
from .entity import Diary


app = Flask(__name__)


@LocalProxy
def session():
    return get_session()


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World'


@app.route('/', methods=['POST'])
def create_diary():
    diary = Diary(subject=request.form['subject'],
                  content=request.form['content'])
    with session.begin():
        session.add(diary)
    return '', 201
