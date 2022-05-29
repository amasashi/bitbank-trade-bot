from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import settings

# 接続先DBの設定
DATABASE = f'{settings.db}://{settings.username}:{settings.password}@{settings.host}:{settings.port}/{settings.database}?charset={settings.charset_type}'

# Engine の作成
engine = create_engine(DATABASE = f'{settings.db}://{settings.username}:{settings.password}@{settings.host}:{settings.port}/{settings.database}?charset={settings.charset_type}')

# Sessionの作成
Session = scoped_session(sessionmaker(bind=engine))

# modelで使用する
Base = declarative_base()
Base.query = Session.query_property()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise        


def init_db():
    Base.metadata.create_all(bind=engine)