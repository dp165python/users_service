from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from core.config import psgres_url

engine = sqlalchemy.create_engine(psgres_url())
Session = sessionmaker(bind=engine)


@contextmanager
def session(auto_commit=True):
    session = Session()
    try:
        yield session
        if auto_commit:
            session.commit()
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()
'''
def dbconnect(func):
    def inner(*args, **kwargs):
        session = Session()  # with all the requirements
        try:
            func(*args, session=session, **kwargs)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    return inner
'''
