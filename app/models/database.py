import logging
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import settings


logger = logging.getLogger(__name__)
engine = create_engine(f'{settings.db}://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.database}')
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = Session.query_property()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        logging.error(f'action=session_scoped error={e}')
        session.rollback()
        raise        


def init_db(drop):
    import app.models.candle
    if drop:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=engine)
    from server.bitbank import Public
    public = Public()
    public.get_candles()

