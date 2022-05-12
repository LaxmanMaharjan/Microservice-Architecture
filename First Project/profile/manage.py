from flask_script import Manager, Server

from server import app

manager = Manager(app)
server = Server(host="127.0.0.1",port=4000)
manager.add_command("runserver",server)

if __name__ == '__main__':
    manager.run()
