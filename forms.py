from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, Form, PasswordField
from wtforms import validators, ValidationError

class LoginForm(Form):
    id = StringField('Username', [validators.DataRequired('Please enter your username.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Login')

class RegisterForm(Form):
    id = StringField('Username', [validators.DataRequired('Please enter your Username.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    answer = StringField('What is your favourite place on Earth?', [validators.DataRequired('Please enter your answer.')])
    submit = SubmitField('Register')

class PasswordForm(Form):
    id = StringField('Username', [validators.DataRequired('Please enter your Username.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    answer = StringField('What is your favourite place on Earth?', [validators.DataRequired('Please enter your answer.')])
    submit = SubmitField('Change Password')

class BlacklistForm(Form):
    id = StringField('Username', [validators.DataRequired('Please enter the username.')])
    reason = StringField('Reason', [validators.DataRequired('Please enter the reason.')])
    submit = SubmitField('Blacklist')