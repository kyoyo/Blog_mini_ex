from flask import render_template, url_for, redirect, flash,request,\
    current_app
from . import main
from app.models import User,Article,ArticleType



@main.route('/',methods=['GET','POST'])
def index():
    page = request.args.get('page',1,type=int)
    pagination = Article.query.order_by(Article.create_time.desc()).paginate(
        page = page,
        per_page = 8
    )

    articles = pagination.items

    return render_template('index.html',articles=articles,pagination=pagination,endpoint='.index')