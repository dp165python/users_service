import unittest
from core.app import app
from tests.data_for_test import test_data, test_data_patch, test_data_put, test_data_auth
import json
from core.config import TestConfig
from core.connector import create_database, drop_database, create_engine, get_engine

'''
import contextlib
from sqlalchemy import MetaData

meta = MetaData()

with contextlib.closing(get_engine().connect()) as con:
    trans = con.begin()
    for table in reversed(meta.sorted_tables):
        con.execute(table.delete())
    trans.commit()
'''

'''
class BaseDatabaseTest(unittest.TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        #env = os.environ.get("test", APP_ENV_TEST)
        app.config.from_object(TestConfig)
        self.app = app.test_client()

        with app.app_context():
            db = create_engine('postgresql://postgres:11111111@localhost:5432/test_users').connect()
            create_database('test_users')

            #db.drop_all()
            #db.create_all()


    def tearDown(self):
        pass
        #with app.app_context():
        #drop_database('test_users')
        #db.session.remove()
        #db.drop_all()


class FlaskTestApi(BaseDatabaseTest):
    
    def setUp(self):
        app.config.from_object(TestConfig())

        # self.app = app.test_client()
        #app.config['TESTING'] = True
        #app.config['WTF_CSRF_ENABLED'] = False
        #app.config['DEBUG'] = False
        #app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB
        self.app = app.test_client()
        #db.init_app(self.app)
        #with app.app_context():
            #db.drop_all()
         #   db.create_all()

        with app.test_request_context():
            #db.drop_all()
            db.create_all()
        #self.assertEqual(app.debug, False)


    def tearDown(self):
        db.session.remove()
        #db.drop_all()
'''

class TestUsersPost(unittest.TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        #env = os.environ.get("test", APP_ENV_TEST)
        app.config.from_object(TestConfig)
        self.app = app.test_client()

        with app.app_context():
            #drop_database('test_users')
            db = create_engine('postgresql://postgres:11111111@localhost:5432/test_users').connect()
            create_database('test_users')

            #db.drop_all()
            #db.create_all()


    def tearDown(self):
        pass
        #with app.app_context():
         #   drop_database('test_users')
        #db.session.remove()
        #db.drop_all()

    '''
    def test_post_user(self):
        user = self.app.post('/users/api/users', json=test_data)
        self.assertEqual(user.status_code, 201)
        self.assertEqual(user.content_type, 'application/json')
    '''

    def test_get_all_users(self):
        users = self.app.get('/users/api/users')
        self.assertEqual(users.status_code, 200)

        content = json.loads(users.get_data(as_text=True))
        self.assertEqual(content, test_data)

    def test_get_user_id(self):
        users = self.app.get('/users/api/744cd7cb-fd8e-4249-a608-db9c4af29b0e')
        self.assertEqual(users.status_code, 404)

        content = json.loads(users.get_data(as_text=True))
        self.assertNotEqual(content, test_data)

    def test_patch(self):
        user = self.app.post(f'/users/api/744cd7cb-fd8e-4249-a608-db9c4af29b0e', json=test_data_patch)
        self.assertEqual(user.status_code, 404)
        self.assertEqual(user.content_type, 'application/json')

    def test_put(self):
        user = self.app.post('/users/api/744cd7cb-fd8e-4249-a608-db9c4af29b0e', json=test_data_put)
        self.assertEqual(user.status_code, 404)
        self.assertEqual(user.content_type, 'application/json')

    def test_authentication(self):
        user = self.app.post('/users/api/authentication', json=test_data_auth)
        self.assertEqual(user.status_code, 404)
        self.assertEqual(user.content_type, 'application/json')

    def test_api_wrong_address(self):
        user = self.app.get('/users/download')
        self.assertEqual(user.status_code, 404)

    def test_post_none_user(self):
        user = self.app.post('/users/api/users/', data=None)
        self.assertEqual(user.status_code, 404)


if __name__ == "__main__":
    unittest.main()
