from functools import wraps

import requests
from flask import request, abort

from core.constants import AUTH_SERVICE_URI


def authentication(func):
    @wraps(func)
    def wraped(*args, **kwargs):
        session = request.form.get('session_id')
        if session:
            response = requests.get(AUTH_SERVICE_URI, params={"sid": session})
            if response.status_code == 200:
                return func(*args, **kwargs)
        abort(400, {"message": "Unauthorized access"})

    return wraped
