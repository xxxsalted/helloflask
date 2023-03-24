import flask_wtf
import wtforms
from wtforms.validators import DataRequired, Length

'''
定义一个登录表单类
'''


class LoginForm(flask_wtf.Form):
    username = wtforms.StringField('Username', render_kw={'placeholder': 'Your Username'}, validators=[DataRequired()])
    password = wtforms.PasswordField('Password', render_kw={'placeholder': 'Your Password'}, validators=[DataRequired(), Length(8, 128)])
    remember = wtforms.BooleanField('Remember me')
    submit = wtforms.SubmitField('Log in')

form = LoginForm()
print(form.username())
print(form.password())