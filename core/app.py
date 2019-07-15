from core.api import usr_api, bp
from core.config import create_app
from core.resources.resources import UsersPutGetPatch, UsersPostGet

app = create_app()
app.register_blueprint(bp, url_prefix='/users')

usr_api.add_resource(UsersPostGet, '/api/users')
usr_api.add_resource(UsersPutGetPatch, '/api/<username>')
