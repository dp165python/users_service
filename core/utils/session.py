from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from ..config import psgres_url

from requests import exceptions

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
    except exceptions.RequestException as e:
        session.rollback()
        raise e
    finally:
        session.close()