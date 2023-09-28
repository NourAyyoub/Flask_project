from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email , EqualTo

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('login')

class SignUpForm(FlaskForm):
    password = PasswordField('Password', validators = [InputRequired()])
    full_name = StringField('Full Name')
    email = StringField('Email',
                        validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
