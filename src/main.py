from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_mail import Message
from flask_wtf import FlaskForm
import os
from wtforms import SelectField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired


app = Flask(__name__)
# Secret key setup
app.config['SECRET_KEY'] = os.environ.get('BIO_DLF_SECRET_KEY')
# Email setup
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('BIO_DLF_MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('BIO_DLF_MAIL_PASSWORD')
app.config['MAIL_SUBJECT_PREFIX'] = 'Someone has submitted feedback!'
app.config['MAIL_SENDER'] = os.environ.get('BIO_DLF_MAIL_USERNAME')
app.config['MAIL_RECEIVER'] = os.environ.get('BIO_DLF_MAIL_RECEIVER')
mail = Mail(app)
# Bootstrap setup
bootstrap = Bootstrap(app)


def send_email(to, subject, template, **kwargs):
    """Call this function when wanting to send an email.  The subject passed in will be prefixed with the value of
    app.config['MAIL_SUBJECT_PREFIX'], so if that needs to be changed change it where it's set above.
    Emails will always be sent from app.config['MAIL_SENDER'].  The recipient needs to be passed in in the to variable.
    The template passed in needs to exist within the templates/mail directory and have both a .html and .txt version."""
    msg = Message(app.config['MAIL_SUBJECT_PREFIX']+subject, sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


class IndexForm(FlaskForm):
    feedback_redirect = SubmitField('Anonymous Feedback')


class FeedbackForm(FlaskForm):
    section = SelectField('Lab Section',
                          choices=[('P01', 'P01 Monday 1:05pm-3:55pm'), ('Q05', 'Q05 Wednesday 1:05pm-3:55pm')])
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    if form.validate_on_submit():
        return redirect(url_for('feedback'))
    return render_template('index.html', form=form)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        # Get the data from the form
        section_data = form.section.data
        feedback_data = form.feedback.data
        # Send an email containing the feedback
        send_email(app.config['MAIL_RECEIVER'], ' '+section_data, 'mail/new_feedback', feedback_data=feedback_data)
        # Tell the user that their feedback was submitted
        flash('Thank you for your feedback!')
        # Go back to the home page
        return redirect(url_for('index'))
    return render_template('feedback.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
