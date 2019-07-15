from werkzeug.security import generate_password_hash, check_password_hash


def set_password(password, user):
    user.hash_password = generate_password_hash(password)
    return user.hash_password


def check_password(hash_password, password):
    return check_password_hash(hash_password, password)


def answer_resource_methods(data):
    return {
            "id": data["id"],
            "username": data["username"],
            "email": data["email"],
            "user_address": data["user_address"],
            "create_user_date": data["create_user_date"]
        }
