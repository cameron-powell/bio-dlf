from flask import current_app, flash, redirect, render_template, url_for
from requests import post
from . import main
from .forms import FeedbackForm, IndexForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    # If the button was clicked go to the feedback page.
    if form.validate_on_submit():
        return redirect(url_for('.feedback'))
    return render_template('index.html', form=form)


@main.route('/feedback', methods=['GET', 'POST'])
def feedback():
    '''Renders the feedback page OR sends the email and redirects
    if it recieves input from the form on the feedback page.'''
    form = FeedbackForm()
    # If the user hit the submit button email their feedback.
    if form.validate_on_submit():
        # Get the data from the form.
        section_data = form.section.data
        feedback_data = form.feedback.data
        # Send an email containing the feedback.
        url = current_app.config['EMAIL_URL']
        auth = ('api', current_app.config['EMAIL_KEY'])
        data = {
            "from": "Anonymous Feedback <"+current_app.config['EMAIL_FROM']+">",
            "to": [current_app.config['EMAIL_TO']],
            "subject": "Someone has submitted feedback! %s" % section_data,
            "text": "" + feedback_data
        }
        response = post(url, data=data, auth=auth)
        # Notify the user of success or failure
        if response.status_code != 200:
            flash('There was an error sending your feedback.  Please try again later...')
        else:
            flash('Thank you for your feedback!')
        # Go back to the home page.
        return redirect(url_for('.index'))
    return render_template('feedback.html', form=form)
