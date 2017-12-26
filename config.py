import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir,'blog.db')
    SQLALCHEMY_RECORD_QUERIES = True
    ARTICLES_PER_PAGE = 10
