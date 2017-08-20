from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class IndexForm(FlaskForm):
    feedback_redirect = SubmitField('Anonymous Feedback')


class FeedbackForm(FlaskForm):
    # The first element of the tuple in 'choices' will be appended to the subject of the email sent
    section = SelectField('Lab Section', choices=[('P2232HPII', 'Physics 2232 - Honors Physics II')])
    # choices=[('P01', 'P01 Monday 1:05pm-3:55pm'), ('Q05', 'Q05 Wednesday 1:05pm-3:55pm')])
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')
