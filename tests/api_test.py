import unittest
from core.app import app
from tests.data_for_test import test_data, test_data_patch, test_data_put, test_data_auth
import json
from core.config import TestConfig
from core.connector import create_database


class TestUsers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.from_object(TestConfig)
        cls.app = app.test_client()
        with app.app_context():
            create_database('test_users')

    def test_post_user(self):
        user = self.app.post('/users/api/users', json=test_data)
        self.assertEqual(user.status_code, 201)
        self.assertEqual(user.content_type, 'application/json')

    def test_get_all_users(self):
        users = self.app.get('/users/api/users')
        self.assertEqual(users.status_code, 200)
        content = json.loads(users.get_data(as_text=True))
        self.assertNotEqual(content, test_data)

    def test_get_user_id(self):
        users = self.app.get('/users/api/744cd7cb-fd8e-4249-a608-db9c4af29b0e')
        self.assertEqual(users.status_code, 404)

        content = json.loads(users.get_data(as_text=True))
        self.assertNotEqual(content, test_data)

    def test_patch(self):
        user = self.app.post(f'/users/api/744cd7cb-fd8e-4249-a608-db9c4af29b0e', json=test_data_patch)
        self.assertNotEqual(user.status_code, 200)
        self.assertEqual(user.content_type, 'application/json')

    def test_put(self):
        user = self.app.post('/users/api/744cd7cb-fd8e-4249-a608-db9c4af29b0e', json=test_data_put)
        self.assertNotEqual(user.status_code, 200)
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
