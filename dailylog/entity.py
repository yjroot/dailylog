import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, Unicode, UnicodeText

from .db import Base


class Diary(Base):
    __tablename__ = 'diary'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        default=datetime.datetime.utcnow)
    subject = Column(Unicode(255), nullable=False)
    content = Column(UnicodeText, nullable=False)
