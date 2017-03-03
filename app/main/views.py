from flask import flash, redirect, render_template, url_for
from . import main
from .forms import FeedbackForm, IndexForm
from ..email import send_email


@main.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    # If the button was clicked go to the feedback page.
    if form.validate_on_submit():
        return redirect(url_for('.feedback'))
    return render_template('index.html', form=form)


@main.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    # If the user hit the submit button email their feedback.
    if form.validate_on_submit():
        # Get the data from the form.
        section_data = form.section.data
        feedback_data = form.feedback.data
        # Send an email containing the feedback.
        send_email(app.config['MAIL_RECEIVER'], ' ' + section_data, 'mail/new_feedback', feedback_data=feedback_data)
        # Tell the user that their feedback was submitted.
        flash('Thank you for your feedback!')
        # Go back to the home page.
        return redirect(url_for('.index'))
    return render_template('feedback.html', form=form)
