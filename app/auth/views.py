from app import db
from . import auth
from flask import render_template,flash,redirect,url_for
from .forms import UserLoginForm,UserRegistForm
from app.models import User
from flask_login import login_user,login_required,logout_user


@auth.route('/login',methods=['GET','POST'])
def login():
    form = UserLoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is not None and user.password == form.password.data:
            login_user(user)
            flash(u'登陆成功！欢迎回来，%s!' % user.username, 'success')

            return redirect(url_for('main.index'))

        else:
            flash(u'登陆失败！用户名或密码错误，请重新登陆。', 'danger')

    return render_template('auth/login.html',form=form)

@auth.route('/regist',methods=['GET','POST'])
def regist():
    form = UserRegistForm()

    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('新增用户成功！','success')

        return redirect(url_for('main.index'))

    return  render_template('auth/regist.html',form=form)

@auth.route('/logout')
#@login_required
def logout():
    logout_user()
    flash(u'您已退出登陆。', 'success')
    return redirect(url_for('main.index'))