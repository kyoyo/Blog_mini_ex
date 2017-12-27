from app import create_app,db
from flask_script import Manager,Server
from database import manager as database_manager



app = create_app()
manager = Manager(app)
manager.add_command('runserver',Server(host='127.0.0.1',port=8000,use_debugger=True))
manager.add_command('database',database_manager)


@manager.command
def show(name,sex):
    print("your name is  %s %s" % (name,sex))

@manager.command
def init_db():
    from app.models import User
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()