from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskFile.models import User

#inherited from FlaskForm class
class RegistrationForm(FlaskForm):
    #The SubmitField class represents an <input> element with a type="submit" attribute.
    # The first argument to the Field constructors is the label that will be used when rendering the form to HTML.
    #These are the attributes of RegestrationForm class
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class Ride(FlaskForm):
    source = StringField('Source', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    date = StringField('Date of Journey', validators=[DataRequired()])
    preference = StringField('Preference')
    submit = SubmitField('Find Ride')
