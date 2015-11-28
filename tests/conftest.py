from pytest import fixture, yield_fixture
from sqlalchemy import create_engine

from dailylog.db import Base, Session
from dailylog import app


TEST_DATABASE_URL = 'sqlite:///test.db'


def get_engine():
    url = app.config['DATABASE_URL'] = TEST_DATABASE_URL
    engine = create_engine(url)
    app.config['DATABASE_ENGINE'] = engine
    return engine


@fixture
def f_app(f_session):
    app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
        DATABASE_URL=TEST_DATABASE_URL
    )
    return app


@yield_fixture
def f_session():
    engine = get_engine()
    try:
        metadata = Base.metadata
        metadata.drop_all(engine)
        metadata.create_all(engine)
        session = Session(bind=engine)
        yield session
        session.rollback()
        metadata.drop_all(engine)
    finally:
        engine.dispose()
