from flask_script import Manager

manager = Manager('table actions')

@manager.command
def select():
    print('select data')

@manager.command
def delete():
    print('delete data')

@manager.command
def insert():
    print('insert data')

@manager.command
def update():
    print('update data')