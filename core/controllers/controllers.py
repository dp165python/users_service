from core.config import bcrypt


def set_password(password, user):
    user.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    return user.password_hash


def check_password(hash_password, password):
    return bcrypt.check_password_hash(hash_password, password)


def answer_resource_methods(data):
    return {
            "id": data["id"],
            "username": data["username"],
            "email": data["email"],
            "user_address": data["user_address"],
            "create_user_date": data["create_user_date"]
        }
