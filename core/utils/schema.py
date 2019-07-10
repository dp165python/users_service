from marshmallow import Schema, fields


class UsersSchema(Schema):
    id = fields.UUID()
    username = fields.Str(required=True, missing=None)
    email = fields.Email(required=True, missing=None)
    password_hash = fields.Str(required=True, missing=None)
    user_address = fields.Str()
    create_user_date = fields.DateTime()

    class Meta:
        fields = ('id', 'username', 'email', 'password_hash', 'user_address', 'create_user_date')


class UsersSchemaPut(Schema):
    username = fields.Str()
    email = fields.Email()
    password_hash = fields.Str()
    user_address = fields.Str()

    class Meta:
        fields = ('username', 'email', 'password_hash', 'user_address')


user_schema_put = UsersSchemaPut()
user_schema = UsersSchema()
