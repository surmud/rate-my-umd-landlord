from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.simple import SubmitField
from wtforms.validators import InputRequired, Length, NumberRange, length, ValidationError


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


#note: I copied and pasted the forms file from p3. We can use this as a model maybe