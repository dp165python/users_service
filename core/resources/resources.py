from flask import request, abort
from flask_restful import Resource

from core.models import Users
from core.utils.schema import user_schema, user_schema_put
#from core.utils.session import session
from core.config import db
from core.controllers.controllers import set_password, check_password, answer_resource_methods


class UsersPostGet(Resource):
    def get(self):
        all_users = db.session.query(Users).all()
        return {'users': user_schema.dump(all_users, many=True).data}

    def post(self):
        data = request.get_json() or {}
        result, errors = user_schema.load(data)
        if errors:
            abort(404, 'Invalid data')

        username = data["username"]
        email = data["email"]
        user_address = data["user_address"]
        password = data["password"]
        user = Users(username=username,
                     email=email,
                     user_address=user_address,
                     password=set_password(password, Users))

        #with session() as ses:
        db.session.add(user)
        db.session.commit()

        usr = db.session.query(Users).filter_by(username=username).first()
        res = user_schema.dump(usr).data
        return answer_resource_methods(res)


class UsersPutGetPatch(Resource):
    def get(self, username):
        user = db.session.query(Users).filter_by(username=username).first()
        data = request.get_json() or {}
        if not user:
            abort(404, 'No user with that name')
        elif data['password'] is None or check_password(user.password, data['password']) is False:
            abort(404, 'Password none or incorrect')

        res = user_schema.dump(user).data
        return answer_resource_methods(res)

    def put(self, username):
        user = db.session.query(Users).filter_by(username=username).first()
        if not user:
            abort(404, 'No user with that name')

        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        if errors:
            abort(404, 'Invalid data')

        db.session.query(Users).filter_by(username=username).update({
                "username": data["username"],
                "email": data["email"],
                "user_address": data["user_address"],
                "password": set_password(data["password"], user)
        })
        db.session.commit()

        res = user_schema.dump(user).data
        return answer_resource_methods(res)

    '''
    def put(self, username):
        user = db.session.query(Users).filter_by(username=username).first()
        if not user:
            abort(404, 'No user with that name')

        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        if errors:
            abort(404, 'Invalid data')

        with session() as ses:
            ses.query(Users).filter_by(username=username).update({
                "username": data["username"],
                "email": data["email"],
                "user_address": data["user_address"],
                "password": set_password(data["password"], user)
            })

        res = user_schema.dump(user).data
        return answer_resource_methods(res)
    '''
    def patch(self, username):
        user = db.session.query(Users).filter_by(username=username).first()
        if not user:
            abort(404, 'No user with that name')

        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        #usern = data['username']
        if errors:
            abort(404, 'Invalid data')
        #with session() as ses:
        for field in ['username', 'email', 'user_address']:
            if field in data:
                db.session.query(Users).filter_by(username=username).update({f"{field}": data[field]})
            if 'password' in data:
                db.session.query(Users).filter_by(username=username).update({
                    "password": set_password(data["password"], user)})
        db.session.commit()

        #user = db.session.query(Users).filter_by(username=usern).first()
        res = user_schema.dump(user).data
        return answer_resource_methods(res)
