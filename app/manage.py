from app import create_app
from flask_script import Manager, Server
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


application = create_app()

manager = Manager(app=application)
manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='localhost',
    port=5000,
    processes=3
))


if __name__ == '__main__':
    manager.run()
