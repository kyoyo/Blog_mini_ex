from app import create_app,db
from flask_script import Manager,Server
from database import manager as database_manager
from flask_migrate import Migrate,MigrateCommand
from app.models import ArticleType,Article,User

app = create_app()
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('runserver',Server(host='127.0.0.1',port=8000,use_debugger=True))
manager.add_command('database',database_manager)
manager.add_command('db',MigrateCommand)

@manager.command
def show(name,sex):
    print("your name is  %s %s" % (name,sex))

@manager.command
def init_db():
    from app.models import User
    db.create_all()
    db.session.commit()

@manager.command
def deploy():
    #User.insert_admin(email='admin@example.com', username='admin', password='admin')
    ArticleType.insert_articleTypes()
    Article.generate_fake(100)

if __name__ == '__main__':
    manager.run()