from core.api import usr_api, bp
from core.config import create_app
from core.resources.resources import UsersPutGetPatch, UsersPostGet

app = create_app()
app.register_blueprint(bp, url_prefix='/users')

usr_api.add_resource(UsersPostGet, '/api/users')
usr_api.add_resource(UsersPutGetPatch, '/api/<username>')

'''
from flask import g
from functools import wraps
from sqlalchemy.orm import sessionmaker
def establish_connection(x_client: str = None):
    def actual_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            g.conn = engine.connect()
            Session = sessionmaker()
            Session.configure(bind=g.conn)
            g.session = Session()
            return func(*args, **kwargs)

        return func_wrapper

    return actual_decorator


def kill_session(e):
    if e is None:
        g.session.commit()
    else:
        g.session.rollback()

    g.session.close()
    g.session = None
'''
