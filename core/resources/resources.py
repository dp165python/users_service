from flask import request, g, abort
from flask_restful import Resource

from core.controllers.controllers import UsersController
from core.controllers.controllers import UsersData
from core.models.models import Users
from core.models.schema import user_schema, user_schema_put, user_schema_patch, user_schema_auth


class UsersResourceCreate(Resource):
    def get(self):
        all_users = UsersController().get_all()
        return [UsersData(usr).answer_resource_methods() for usr in all_users], 200

    def post(self):
        data = request.get_json() or {}
        result, errors = user_schema.load(data)
        user_check_post = UsersController().post_user(result, errors)
        controll_check = g.session.query(Users).filter(Users.username == user_check_post).first()
        return UsersData(controll_check).answer_resource_methods(), 201


class UsersResourceChange(Resource):
    def put(self, id):
        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        user_check_put = UsersController().put_user(id, result, errors)
        return UsersData(user_check_put).answer_resource_methods(), 200

    def patch(self, id):
        data = request.get_json() or {}
        result, errors = user_schema_patch.load(data)
        user_check_patch = UsersController().patch_user(id, result, errors)
        return UsersData(user_check_patch).answer_resource_methods(), 200

    def get(self, id):
        user = UsersController().get_user(id)
        return UsersData(user).answer_resource_methods(), 200


class UsersResourceAuth(Resource):
    def post(self):
        data = request.get_json() or {}
        result, errors = user_schema_auth.load(data)
        user_check_auth = UsersController().post_auth(result, errors)
        return UsersData(user_check_auth).answer_resource_methods(), 200
