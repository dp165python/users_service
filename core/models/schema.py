from marshmallow import Schema, fields


class UsersSchema(Schema):
    id = fields.UUID()
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    user_address = fields.Str(required=True)
    create_user_date = fields.DateTime()

    class Meta:
        fields = ('id', 'username', 'email', 'password', 'user_address', 'create_user_date')


class UsersSchemaPut(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    user_address = fields.Str(required=True)

    class Meta:
        fields = ('username', 'email', 'password', 'user_address')


class UsersSchemaPatch(Schema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    user_address = fields.Str()

    class Meta:
        fields = ('username', 'email', 'password', 'user_address')


class UsersSchemaAuth(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    class Meta:
        fields = ('username', 'password')


user_schema_put = UsersSchemaPut()
user_schema = UsersSchema()
user_schema_patch = UsersSchemaPatch()
user_schema_auth = UsersSchemaAuth()
