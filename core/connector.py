from threading import Lock

from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool
from sqlalchemy_utils import database_exists
from core.models.models import Base

engine_lock = Lock()
engine = None


def get_db_uri(user=None, password=None, host=None, port=None, db_name=None):
    return current_app.config['DB_URI'].format(
        user=user or current_app.config['DB_USER'],
        password=password or current_app.config['DB_PASSWORD'],
        host=host or current_app.config['DB_HOST'],
        port=port or current_app.config['DB_PORT'],
        db_name=db_name or current_app.config['DB_NAME'],
    )


def get_engine(uri):
    global engine

    with engine_lock:

        if not engine:
            engine = create_engine(uri, poolclass=QueuePool)
        try:
            engine.execute('select 1')
        except SQLAlchemyError as e:
            engine = create_engine(uri, poolclass=QueuePool)
    return engine


def get_connection():
    return get_engine(get_db_uri()).connect()


def create_database(db_name: str = None):
    default_engine = create_engine(
        get_db_uri(db_name=current_app.config['DEFAULT_DB']), poolclass=NullPool, isolation_level='AUTOCOMMIT'
    )
    db_name = db_name or current_app.config['DB_NAME']
    db_engine = get_engine(get_db_uri(db_name=db_name))

    if not database_exists(db_engine.url):
        default_engine.execute(f'create database {db_name}')
        default_engine.dispose()

    Base.metadata.create_all(db_engine)
    db_engine.dispose()


def drop_database(db_name: str = None):
    default_engine = create_engine(
        get_db_uri(db_name=current_app.config['DEFAULT_DB']), poolclass=NullPool, isolation_level='AUTOCOMMIT'
    )
    db_name = db_name or current_app.config['   DB_NAME']

    if database_exists(default_engine.url):
        default_engine.execute(f'drop database {db_name}')
        default_engine.dispose()
