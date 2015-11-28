from flask import url_for as flask_url_for

from dailylog.app import app
from dailylog.entity import Diary


def url_for(url, **kwargs):
    with app.test_request_context():
        return flask_url_for(url, **kwargs)


def test_create_diary(f_app, f_session):
    before_count = f_session.query(Diary).count()
    with f_app.test_client() as client:
        response = client.post(url_for('create_diary'),
                               data={'subject': 'macmorning',
                                     'content': 'matitda'})
    assert response.status_code == 201
    assert f_session.query(Diary).count() == before_count + 1
    diary = f_session.query(Diary).order_by(Diary.id.desc()).first()
    assert diary.subject == 'macmorning'
    assert diary.content == 'matitda'


def test_create_diary_bad_request(f_app):
    with f_app.test_client() as client:
        response = client.post(url_for('create_diary'), data={})
    assert response.status_code == 400
