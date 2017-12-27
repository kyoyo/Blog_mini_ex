from flask import Blueprint,render_template,url_for,redirect,flash
from .forms import UserForm
from .models import User
from . import db

main = Blueprint('main',__name__)

@main.route('/',methods=['GET','POST'])
def index():
    form = UserForm()
    user_list = User.query.all()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Success!','success')

        return redirect(url_for('main.index'))

    return render_template('index.html',form=form,user_list=user_list)