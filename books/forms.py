from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from books.models import Users


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "username"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "email address"})
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "password"})
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "confirm password"})
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "email address"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# class SearchForm(FlaskForm):
    # isbn = StringField('isbn_number', validators=[DataRequired()])
    # title = StringField('title', validators=[DataRequired()])
    # author = StringField('author', validators=[DataRequired()])
    # submit = SubmitField('Search')