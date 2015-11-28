import datetime

from dailylog.entity import Diary


def test_diary(f_session):
    diary = Diary(subject='today', content='helloworld')
    with f_session.begin():
        f_session.add(diary)
    assert diary.id
    assert diary.created_at
    assert isinstance(diary.created_at, datetime.datetime)
    assert diary.subject == 'today'
    assert diary.content == 'helloworld'
