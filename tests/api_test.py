import unittest
from core.app import app
from tests.data_for_test import data_all_users, test_data_post
import json
from core.config import TestConfig
from core.connector import create_database, drop_database, create_engine
#from tests.fixtures import sample
#from flask_fixtures import FixturesMixin

'''
FixturesMixin.init_app(app, db)
fixtures = 'users_test_data.json'
'''

class BaseDatabaseTest(unittest.TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        #env = os.environ.get("test", APP_ENV_TEST)
        #fixtures = os.path.join(BASE_DIR, 'users_test_data.json')
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

'''
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

class TestUsersPost(BaseDatabaseTest):
    def test_post_user(self):
        #user = self.app.post('/users/api/users', data=json.dumps(self.test_data), content_type='application/json')
        #with self.client:
            user = self.app.post('/users/api/users', json=test_data_post)
            self.assertEqual(user.status_code, 201)
            self.assertEqual(user.content_type, 'application/json')


class TestUsersGetAll(BaseDatabaseTest):
    def test_post_user(self):
        #user = self.app.post('/users/api/users', data=json.dumps(test_data_post), content_type='application/json')
        user = self.app.post('/users/api/users', json=test_data_post)
        self.assertEqual(user.status_code, 201)
        self.assertEqual(user.content_type, 'application/json')
        return user.data

    #data = test_post_user
    #print(data)

    def test_get_all_users(self):
        users = self.app.get('/users/api/users')
        self.assertEqual(users.status_code, 200)

        content = json.loads(users.get_data(as_text=True))
        self.assertEqual(content, self.data)

'''
    def test_get_user_without_password(self):
        user = self.app.get('/users/api/alice')
        self.assertEqual(user.status_code, 404)

        content = json.loads(user.get_data(as_text=True))
        self.assertEqual(content, {'Error': "'password'"})

    def test_get_none_user_404(self):
        user = self.app.get('/users/api/don')
        self.assertEqual(user.status_code, 404)

    def test_post_none_user(self):
        user = self.app.post('/users/api/users/', data=None)
        self.assertEqual(user.status_code, 404)

    def test_api_wrong_address(self):
        user = self.app.get('/users/download')
        self.assertEqual(user.status_code, 404)
'''

if __name__ == "__main__":
    unittest.main()
