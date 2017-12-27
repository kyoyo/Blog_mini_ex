from .import db,login_manager
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable =False)
    username = db.Column(db.String(64), unique=True,nullable=False)
    password = db.Column(db.String(128))


    @staticmethod
    def insert_admin(email, username, password):
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()


    def __repr__(self):
        return '<User %r>' % self.username

'''
ArticleType:
-id
-name
-introduction
-articles
'''

class ArticleType(db.Model):
    __tablename__ = 'articleTypes'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,nullable=False)
    introduction = db.Column(db.Text,default=None)
    articles = db.relationship('Article',backref='articleType',lazy='dynamic')

    def __repr__(self):
        return '<Type %r>' % self.name

    @staticmethod
    def insert_system_articleType():
        articleType = ArticleType(name=u'未分类',
                                  introduction=u'系统默认分类，不可删除。'
                                  )
        db.session.add(articleType)
        db.session.commit()

    @staticmethod
    def insert_articleTypes():
        articleTypes = ['Python', 'Java', 'JavaScript', 'Django',
                        'CentOS', 'Ubuntu', 'MySQL', 'Redis',
                        u'Linux成长之路', u'Linux运维实战', u'其它',
                        u'思科网络技术', u'生活那些事', u'学校那些事',
                        u'感情那些事', 'Flask']
        for name in articleTypes:
            articleType = ArticleType(name=name)
            db.session.add(articleType)
        db.session.commit()

'''
Article:
-id
-title
-content
-summary
-create_time
-update_time
-num_of_view
-articleType_id
'''
class Article(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64),unique=True)
    content = db.Column(db.Text)
    summary = db.Column(db.Text)
    create_time = db.Column(db.DateTime,default=datetime.utcnow)
    update_time = db.Column(db.DateTime,default=datetime.utcnow)
    num_of_view = db.Column(db.Integer,default=0)
    articleType_id = db.Column(db.Integer,db.ForeignKey('articleTypes.id'))

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed, randint
        import forgery_py

        seed()
        articleType_count = ArticleType.query.count()

        for i in range(count):
            aT = ArticleType.query.offset(randint(0, articleType_count - 1)).first()
            a = Article(title=forgery_py.lorem_ipsum.title(randint(3, 5)),
                        content=forgery_py.lorem_ipsum.sentences(randint(15, 35)),
                        summary=forgery_py.lorem_ipsum.sentences(randint(2, 5)),
                        num_of_view=randint(100, 15000),
                        articleType=aT)
            db.session.add(a)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

    def __repr__(self):
        return '<Article %r>' % self.title


# callback function for flask-login extentsion
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))