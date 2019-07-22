from flask import abort, g
from werkzeug.security import generate_password_hash, check_password_hash

from core.models.models import Users


def set_password(password, user):
    user.hash_password = generate_password_hash(password)
    return user.hash_password


def check_password(hash_password, password):
    return check_password_hash(hash_password, password)


class UsersData:
    def __init__(self, user):
        self._user = user

    def answer_resource_methods(self):
        return {
            'id': str(self._user.id),
            'username': self._user.username,
            'email': self._user.email,
            'user_address': self._user.user_address,
            'create_user_date': self._user.create_user_date
        }


class UsersController:
    def get_all(self):
        all_users = g.session.query(Users).all()
        if not all_users:
            abort(404, 'No users')
        return all_users

    def post_user(self, data, errors):
        if errors:
            abort(404, f'Invalid data: {errors}')

        username = data["username"]
        email = data["email"]
        user_address = data["user_address"]
        password = set_password(data["password"], Users)

        user = Users(username=username, email=email, password=password, user_address=user_address)
        g.session.add(user)
        return username

    def put_user(self, id, data, errors):
        user = g.session.query(Users).filter(Users.id == id).first()
        if not user:
            abort(404, 'No user with that id')

        if errors:
            abort(404, f'Invalid data{errors}')

        user.username = data["username"]
        user.email = data["email"]
        user.user_address = data["user_address"]
        user.password = set_password(data["password"], Users)
        return user

    def patch_user(self, id, data, errors):
        user = g.session.query(Users).filter(Users.id == id).first()
        if not user:
            abort(404, 'No user with that name')
        if errors:
            abort(404, f'Invalid data{errors}')

        if 'username' in data:
            user.username = data["username"]
        if 'email' in data:
            user.email = data["email"]
        if 'user_address' in data:
            user.user_address = data["user_address"]
        if 'password' in data:
            user.password = set_password(data["password"], user)
        return user

    def get_user(self, id):
        user = g.session.query(Users).filter(Users.id == id).first()
        if not user:
            abort(404, 'No user with that id')
        return user

    def post_auth(self, data, errors):
        if errors:
            abort(404, f'Invalid data{errors}')

        username = data['username']
        user = g.session.query(Users).filter(Users.username == username).first()
        if not user:
            abort(404, 'No user with that id')

        password = check_password(user.password, data['password'])
        if username != user.username or password is False:
            abort(404, 'Incorrect username or password')
        return user
