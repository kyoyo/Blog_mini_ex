from flask_wtf import Form
from wtforms import StringField,IntegerField,SubmitField,SelectField,RadioField,BooleanField
from wtforms.validators import InputRequired,Email

class UserForm(Form):
    username = StringField('username',[InputRequired()])
    email = StringField('email',[InputRequired(),Email()])
    #sex = SelectField(choices=[('0','male'),('1','female')])
    #nation = RadioField(choices=[('0','China'),('1','Japan'),('2','US')])
    #isRemembered = BooleanField('Remember',description='check it to remember')

    submit_button = SubmitField('Submit')
