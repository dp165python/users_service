from flask_migrate import MigrateCommand
from flask_script import Manager

from core.app import app


manager = Manager(app)


@manager.option('-p', '--port', help='Server port')
@manager.option('-h', '--host', help='Server host')
def runserver(host, port):
    manager.add_command('migrate_db', MigrateCommand)
    app.run(host, port, debug=True)


if __name__ == '__main__':
    manager.run()
