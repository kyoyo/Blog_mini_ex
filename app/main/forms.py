# from flask_wtf import Form
# from wtforms import StringField,IntegerField,SubmitField,SelectField,RadioField,BooleanField,PasswordField
# from wtforms.validators import InputRequired,Length,Email
#
# class UserForm(Form):
#     username = StringField('用户名',[InputRequired('用户名不能为空'),Length(1,10,message='长度必须在1到10之间')])
#     email = StringField('邮件地址',[InputRequired('邮件不能为空'),Length(1,50),Email(message='邮件格式不对')])
#     password = PasswordField('密码',[InputRequired()])
#     #sex = SelectField(choices=[('0','male'),('1','female')])
#     #nation = RadioField(choices=[('0','China'),('1','Japan'),('2','US')])
#     #isRemembered = BooleanField('Remember',description='check it to remember')
#
#     submit_button = SubmitField('新增用户')
