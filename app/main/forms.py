from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class IndexForm(FlaskForm):
    feedback_redirect = SubmitField('Anonymous Feedback')


class FeedbackForm(FlaskForm):
    section = SelectField('Lab Section', choices=[('P2211SOUP', 'Physics 2211 SOUP')])
    # choices=[('P01', 'P01 Monday 1:05pm-3:55pm'), ('Q05', 'Q05 Wednesday 1:05pm-3:55pm')])
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')
