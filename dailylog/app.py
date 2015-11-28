import json

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


@app.route('/<int:diary_id>', methods=['GET'])
def read_diary(diary_id):
    diary = session.query(Diary).filter(Diary.id == diary_id).first()
    if diary is None:
        return 'No diary', 404

    return json.dumps({'subject': diary.subject,
                       'content': diary.content})
