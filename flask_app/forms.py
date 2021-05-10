from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import InputRequired, Length, NumberRange, length, ValidationError, Email, EqualTo
from .models import User

class SearchForm(FlaskForm):
    search_query = StringField("Name:", validators=[InputRequired(), Length(min=1, max = 30)])
    submit = SubmitField("Submit")

class MovieReviewForm(FlaskForm):
    try:
        name = StringField("Enter Your Name:", validators=[InputRequired(), Length(min=1, max = 50)])
        text = TextAreaField("Type your review:", validators=[InputRequired(), Length(min=1, max = 500)])
        submit = SubmitField("Submit")
    except ValidationError as err:
        err_msg = str(err)


class LandlordReviewForm(FlaskForm):
    try:
        name = StringField("Enter Your Name:", validators=[InputRequired(), Length(min=1, max = 50)])
        landlordName = StringField("Enter Your Landlord's Name:", validators=[InputRequired(), Length(min=1, max = 50)])
        address = StringField("Enter The Adress of the Place You Lived:", validators=[InputRequired(), Length(min=1, max = 100)])
        landlordReview = TextAreaField("How was your landlord?", validators=[InputRequired(), Length(min=1, max = 500)])
        propertyReview = TextAreaField("How was the property?", validators=[InputRequired(), Length(min=1, max = 500)])
        submit = SubmitField("Submit")
    except ValidationError as err:
        err_msg = str(err)

class RegisterForm(FlaskForm):
    username = StringField("Enter a username:", validators=[InputRequired(), Length(min=1, max=32)])
    email = StringField("Enter your email:", validators=[InputRequired(), Email()])
    password = PasswordField("Enter a password:", validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")

class LoginForm(FlaskForm):
    username = StringField("Enter your username:", validators=[InputRequired(), Length(min=1, max=32)])
    password = PasswordField("Enter your password:", validators=[InputRequired()])
    submit = SubmitField("Login")

class UpdateUsernameForm(FlaskForm):
    username = StringField("Enter your new username:", validators=[InputRequired(), Length(min=1, max=32)])
    submit = SubmitField("Change Password")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

class UpdatePasswordForm(FlaskForm):
    password = PasswordField("Enter a new password:", validators=[InputRequired()])
    submit = SubmitField("Change Password")

#note: I copied and pasted the forms file from p3. We can use this as a model maybe