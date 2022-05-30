import logging
from psycopg2 import Timestamp

from sqlalchemy import Column
from sqlalchemy import TIMESTAMP
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.exc import IntegrityError

from app.models.database import Base
from app.models.database import session_scope

logger = logging.getLogger(__name__)


class Candle(Base):
    __tablename__ = 'candle'
    time = Column(TIMESTAMP, primary_key=True, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    vol = Column(Float)

    @classmethod
    def create(cls, time, open, high, low, close, vol):
        candle = cls(time=time,
                     open=open,
                     high=high,
                     low=low,
                     close=close,
                     vol=vol)
        try:
            with session_scope() as session:
                session.add(candle)
            return candle
        except IntegrityError:
            return False

    @classmethod
    def get(cls, time):
        with session_scope() as session:
            candle = session.query(cls).filter(
                cls.time == time).first()
            if candle is None:
                return None
            return candle

    def save(self):
        with session_scope() as session:
            session.add(self)

    