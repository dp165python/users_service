# from core.api import usr_api, bp
from core.resources.resources import UsersResourceCreate, UsersResourceChange, UsersResourceAuth

from core.config import runtime_config
from flask_restful import Api
from flask import Flask, g
from sqlalchemy.orm import sessionmaker
from core.connector import get_connection
from core.utils.response import MyResponse

app = Flask(__name__)
app.config.from_object(runtime_config())
app.response_class = MyResponse


@app.before_request
def open_session():
    g.conn = get_connection()
    session = sessionmaker()
    session.configure(bind=g.conn)
    g.session = session()


@app.teardown_request
def close_session(e):
    if 'session' in g:
        if e is None:
            g.session.commit()
        else:
            g.session.rollback()

        g.session.close()
        g.session = None


api = Api(app, prefix='/users')

#app.register_blueprint(bp, url_prefix='/users')

api.add_resource(UsersResourceCreate, '/api/users')
api.add_resource(UsersResourceChange, '/api/<id>')
api.add_resource(UsersResourceAuth, '/api/authentication')
